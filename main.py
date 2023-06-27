#pip install snowflake-connector-python

import snowflake.connector
import time
import pandas as pd
import datetime
import pytz
# import configparser
# import subprocess


def send_mail(DF,result):
    print("Sending mail...")
    time.sleep(3)
    if result==1:
      print(DF)
    else:
      print(DF)

def load_in_hist(cursor,df):
  pass
#   stage_name = 'tmp_stage'
#   cursor().execute(f'CREATE TEMPORARY STAGE {stage_name}')
#   csv_path = 'df.csv'
#   df.to_csv(csv_path, index=False)
#   cursor().execute(f'PUT file://{csv_path} @{stage_name}')
#   target_table = 'test_result_hist'
#   merge_query = f'''
#     MERGE INTO {target_table} AS t
#     USING (SELECT * FROM @{stage_name}/df.csv) AS s
#     ON (t.name = s.output)
#     WHEN MATCHED THEN
#         UPDATE SET t.name = s.output
#     WHEN NOT MATCHED THEN
#         INSERT (name, test_name,expected_output,output,last_update,flag,result) VALUES (s.name, s.test_name,s.expected_output,s.output,s.last_update,s.flag,s.result)
# '''
#   cursor().execute(merge_query)

# Remove the temporary stage
  # cursor().execute(f'DROP STAGE {stage_name}')
  # print("process done")



def trigger_nba():
    # script_path = r'C:\path\to\your\script.ps1'
    # process = subprocess.Popen(['powershell.exe', '-ExecutionPolicy', 'Bypass', '-File', script_path], stdout=subprocess.PIPE)
    # output, error = process.communicate()
    # print(output.decode('utf-8'))
    global NBA_flag
    NBA_flag = 1
    print("NBA triggered successfully.........................................")


def trigger_inforce():
    # script_path = r'C:\path\to\your\script.ps1'
    # process = subprocess.Popen(['powershell.exe', '-ExecutionPolicy', 'Bypass', '-File', script_path], stdout=subprocess.PIPE)
    # output, error = process.communicate()
    # print(output.decode('utf-8'))
    global INFORCE_flag
    INFORCE_flag = 1
    print("INFORCE triggered successfully.....................................")


def test_nba(cursor):
    print("NBA TEST started")
    time.sleep(3)
    cursor.execute("SELECT * FROM test_result where name='NBA'")
    column_names = [description[0] for description in cursor.description]
    test1 = cursor.fetchall()
    df = pd.DataFrame(test1, columns=column_names)
    df['RESULT'] = ['PASS' if expected == output else 'FAIL' for expected, output in zip(df['EXPECTED_OUTPUT'], df['OUTPUT'])]
    load_in_hist(cursor,df)
    if 'PASS' in df['RESULT'].values:
      print("NBA TEST PASSED")
      send_mail(df,1)
      return 'PASS'
    else:
        print("NBA TEST FAILED")
        send_mail(df,0)
        global NBA_flag
        NBA_flag = 1
        return 'Failed'

def test_inforce(cursor):
    print("INFORCE TEST started")
    time.sleep(3)
    test_dict = []
    cursor.execute("SELECT * FROM test_result where name='INFORCE'")
    column_names = [description[0] for description in cursor.description]
    test1 = cursor.fetchall()
    df = pd.DataFrame(test1, columns=column_names)
    df['RESULT'] = ['PASS' if expected == output else 'FAIL' for expected, output in zip(df['EXPECTED_OUTPUT'], df['OUTPUT'])]
    if 'PASS' in df['RESULT'].values:
      print("INFORCE TEST PASSED")
      send_mail(df,1)
      return 'PASS'
    else:
        print("INFORCE TEST FAILED")
        send_mail(df,0)
        global INFORCE_flag
        INFORCE_flag = 1
        return 'Failed'


def nba_test_and_trigger(cursor):
    if test_nba(cursor) == 'PASS':
        time.sleep(3)
        trigger_nba()
    else:
        time.sleep(3)


def inforce_test_and_trigger(cursor):
    if test_inforce(cursor) == 'PASS':
        time.sleep(3)
        trigger_inforce()
    else:
        time.sleep(3)


def initialize_flags():
    global NBA_flag, INFORCE_flag
    NBA_flag = 0
    INFORCE_flag = 0


def connect_to_snowflake(account, user, password, database, warehouse, schema):
    try:
        conn = snowflake.connector.connect(
            account=account,
            user=user,
            password=password,
            database=database,
            warehouse=warehouse,
            schema=schema
        )
        return conn
    except:
        print("Snowflake connection failed")


def check_load_completion(conn):
    from datetime import datetime
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM test_result")
        column_names = [description[0] for description in cursor.description]
        results = cursor.fetchall()
        print("Connection established, query in progress...")
    except:
        print("Snowflake connection failed")
        return {}

    df = pd.DataFrame(results, columns=column_names)
    dct = {}
    date_obj = datetime.now().date()
    global LOAD1, LOAD2
    LOAD1 = 'NBA' + date_obj.strftime("%d%m")
    LOAD2 = 'INFORCE' + date_obj.strftime("%d%m")
    if not df.empty:
        try:
            selected_name = df.loc[df['FLAG'] == LOAD1, 'FLAG'].values[0]
            dct['NBA_DONE'] = selected_name
        except (KeyError, IndexError):
            dct['NBA_DONE'] = 'NULL'


        try:
            selected = df.loc[df['FLAG'] == LOAD2, 'FLAG'].values[0]
            dct['INFORCE'] = selected
        except (KeyError, IndexError):
            dct['INFORCE'] = 'NULL'
    else:
        dct['NBA_DONE'] = 'NULL'
        dct['INFORCE'] = 'NULL'

    return dct


def main():
    # Set up configuration
    # config = configparser.ConfigParser()
    # config.read('config.ini')
    # Snowflake connection parameters
    account = 'rnxicum-bs93556'
    user = 'SMarkam'
    password = 'Edith@123'
    database = 'TRAINING'
    warehouse = 'TRANSFORMING'
    schema = 'TRAINING'

    # Set flag to avoid multiple triggers in a day
    initialize_flags()

    # Connect to Snowflake
    conn = connect_to_snowflake(account, user, password, database, warehouse, schema)

    # Create a cursor
    cursor = conn.cursor()

    # Infinitely loop to check load status
    while True:
        try:
            dct = check_load_completion(conn)
            if dct['NBA_DONE'] == LOAD1 and NBA_flag == 0:
                print("NBA loads completed")
                time.sleep(3)
                print("Starting NBA test")
                time.sleep(3)
                nba_test_and_trigger(cursor)

            if dct['INFORCE'] == LOAD2 and INFORCE_flag == 0:
                print("INFORCE loads completed")
                time.sleep(3)
                print("Starting INFORCE test")
                time.sleep(3)
                inforce_test_and_trigger(cursor)

            # Reset the flag (Every day at 9 PST)
            current_time = datetime.datetime.now(pytz.timezone('US/Pacific'))
            if current_time.hour == 9:
                initialize_flags()
            time.sleep(8)
        except KeyboardInterrupt:
            print("process interrupted")
            break


if __name__ == '__main__':
    main()
