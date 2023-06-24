
-- --this table will indicate the job completion
-- create or replace table TRAINING.TRAINING.thirdrdquery(
-- name varchar(20),
-- time date
-- );

-- truncate table thirdrdquery;
-- insert into thirdrdquery values('NBA',to_date(current_timestamp));
-- insert into thirdrdquery values('INFORCE',to_date(current_timestamp));

-- select * from TRAINING.TRAINING.thirdrdquery;



--================NBA?INFORCE=======================================================

--nba demo table for tasting
create or replace table TRAINING.TRAINING.nba(
name varchar(8),
flag varchar(8)
);
insert into TRAINING.TRAINING.nba values('sa','ba');
select * from nba;

create or replace table TRAINING.TRAINING.INFORCE(
name varchar(20),
flag varchar(20)
);
insert into TRAINING.TRAINING.INFORCE values('th','ba');
select * from INFORCE;






-- Create the ql_queries table
CREATE or replace TABLE sql_queries (
  query_id INT AUTOINCREMENT,
  query_text VARCHAR(1000)
);

truncate table sql_queries;

-- Insert dummy values into the ql_queries table
INSERT INTO sql_queries (query_text)
VALUES('SELECT count(*) FROM inforce;');



select * from sql_queries;





CREATE OR REPLACE TABLE test_result (
  name VARCHAR,
  test_name VARCHAR,
  expected_output VARCHAR,
  output VARCHAR,
  last_update DATE ,
  flag varchar
);

INSERT INTO test_result (name, test_name, expected_output, output,last_update)
VALUES
  ('NBA', 'Test 1', 3, null,null),
  ('INFORCE', 'Test 2', 2,  null,null);
update test_result set output= 3, last_update=current_date,flag ='NBA'||TO_CHAR(current_date, 'DDMMYYYY') where name='NBA' and  test_name='Test 1';




  select * from test_result;

--select query_text from sql_queries;
CREATE OR REPLACE PROCEDURE nba()
RETURNS STRING
LANGUAGE JAVASCRIPT
AS
$$
var statement = `select query_text from sql_queries;`;
var statement1 = snowflake.createStatement({
    sqlText: statement
})
var contract_ids = statement1.execute();
const contract_lst = [];
while (contract_ids.next()) {
    var value1 = contract_ids.getColumnValue(1);
    contract_lst.push(value1);
};


var statement2 = contract_lst[0];
var statement3 = snowflake.createStatement({
    sqlText: statement2
})
var contracts = statement3.execute();
const contract = [];
while (contracts.next()) {
    var value2 = contracts.getColumnValue(1);
    contract.push(value2);
};

var statement11 = `update test_result set output=`+contract[0]+`, last_update=current_date,flag ='NBA'||TO_CHAR(current_date, 'DDMM') where name='NBA' and  test_name='Test 1';`;
var statement12 = snowflake.createStatement({
        sqlText: statement11
    })
    try{
    snowflake. execute({
      sqlText:statement11
        });
       
    }
    catch(err){
    return err;
    };

 
return "Test template refreshed for NBA";
$$;


call nba();
  select * from test_result;


CREATE OR REPLACE PROCEDURE inforce()
RETURNS STRING
LANGUAGE JAVASCRIPT
AS
$$
var statement = `select query_text from sql_queries;`;
var statement1 = snowflake.createStatement({
    sqlText: statement
})
var contract_ids = statement1.execute();
const contract_lst = [];
while (contract_ids.next()) {
    var value1 = contract_ids.getColumnValue(1);
    contract_lst.push(value1);
};


var statement2 = contract_lst[1];
var statement3 = snowflake.createStatement({
    sqlText: statement2
})
var contracts = statement3.execute();
const contract = [];
while (contracts.next()) {
    var value2 = contracts.getColumnValue(1);
    contract.push(value2);
};

var statement11 = `update test_result set output=`+contract[0]+`, last_update=current_date,flag ='INFORCE'||TO_CHAR(current_date, 'DDMM') where name='INFORCE' and  test_name='Test 2';`;
var statement12 = snowflake.createStatement({
        sqlText: statement11
    })
    try{
    snowflake. execute({
      sqlText:statement11
        });
       
    }
    catch(err){
    return err;
    };

 
return "Test template refreshed for INFORCE";
$$;

call inforce();
  select * from test_result;

CREATE OR REPLACE TABLE test_result_hist (
  name VARCHAR,
  test_name VARCHAR,
  expected_output VARCHAR,
  output VARCHAR,
  last_update DATE ,
  flag varchar
);



select * from test_result_hist;



insert into test_result_hist select * from test_result where NAME='INFORCE';

--=========================================================================================================


--loads
select * from nba;--3 rec
select * from INFORCE;--1 record


--test queries 
select * from sql_queries;


--
select * from test_result;--test template
call nba();--prcedure to update templete for NBA
call inforce();--prcedure to update templete for INFORCE



select * from test_result_hist;







update test_result
set OUTPUT=null,LAST_UPDATE=null,FLAG=null
where NAME in ('INFORCE','NBA');

  

