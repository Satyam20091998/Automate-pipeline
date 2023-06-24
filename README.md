**AUTOMATE TRIGGER WITH TESTING**

_#created by: - Satyam Markam_

_#Date: -16-06-2023_

_#language: SQL, Python_

**Table Details:**

**1.SQL query table**

- Test case SQL queries are stored in a table.
- The procedure utilizes this table to generate the test output.

**2. Test template**

- The table has a fixed number of columns and rows, serving as a template.
- A procedure will fill the table with output specific to the current date.
- Python will then utilize this table to trigger the tableau subscription.

**3. history table**

- Store daily test results.
- Perform monthly analysis using the stored data.

**1. SQL query table**

![Picture 1](RackMultipart20230624-1-kvihc1_html_446d9b86ff239d3d.gif)

**2. Test template**

![Picture 2](RackMultipart20230624-1-kvihc1_html_89a75370ce65e9d9.gif)

**3 history table**

![Picture 3](RackMultipart20230624-1-kvihc1_html_b78729ee9678610a.gif)

![Shape1](RackMultipart20230624-1-kvihc1_html_fc62ff6558a1ef42.gif) **Flow:**

![Shape2](RackMultipart20230624-1-kvihc1_html_5b1c993483961538.gif) ![Shape3](RackMultipart20230624-1-kvihc1_html_81199e73e258322e.gif)

![Shape5](RackMultipart20230624-1-kvihc1_html_21a7a8623be9dc22.gif) ![Shape4](RackMultipart20230624-1-kvihc1_html_21a7a8623be9dc22.gif)

Python

SNOWFLAKE

**Steps:**

1. Load completion triggers the procedure.
2. The procedure updates the template with current date testing result.
3. Python validates and sends confirmation emails to users.

**Python Flow:**

![Shape8](RackMultipart20230624-1-kvihc1_html_909a5adfd70c04af.gif) ![Shape9](RackMultipart20230624-1-kvihc1_html_909a5adfd70c04af.gif) ![Shape7](RackMultipart20230624-1-kvihc1_html_5804f6d3fe820d09.gif) ![Shape6](RackMultipart20230624-1-kvihc1_html_2a3859eaaab38b21.gif)

**Load completed.**

CHECK SNOWFALKE TEST TEMPLATE

**TEST TEMPLETE UPDATE**

PYTHON TRIGGER

![Shape19](RackMultipart20230624-1-kvihc1_html_c64fcb3e908e7b18.gif) ![Shape16](RackMultipart20230624-1-kvihc1_html_e55a10afcf61d07e.gif) ![Shape20](RackMultipart20230624-1-kvihc1_html_ee430a0a40d3a1aa.gif) ![Shape17](RackMultipart20230624-1-kvihc1_html_311fbca30880a60a.gif) ![Shape18](RackMultipart20230624-1-kvihc1_html_7b5b181652f4ce4.gif) ![Shape15](RackMultipart20230624-1-kvihc1_html_9385a0dc8d100fcd.gif) ![Shape14](RackMultipart20230624-1-kvihc1_html_2ec51d6c94cb9410.gif) ![Shape13](RackMultipart20230624-1-kvihc1_html_39c8169899e5062d.gif) ![Shape11](RackMultipart20230624-1-kvihc1_html_6802af5e1ef72280.gif) ![Shape12](RackMultipart20230624-1-kvihc1_html_6802af5e1ef72280.gif) ![Shape10](RackMultipart20230624-1-kvihc1_html_6802af5e1ef72280.gif)

TEST FAILED

Send mail.

TEST PASS

Trigger tableau

Send mail.
