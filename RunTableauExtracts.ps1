# Path to Tableau Desktop installation
$TableauPath = "C:\Program Files\Tableau\Tableau <Version>\bin\tableau.exe"

# Path to the Tableau workbook (.twb or .twbx) file
$WorkbookPath = "C:\Path\to\Workbook.twbx"

# Path to the Tableau extract (.tde) file
$ExtractPath = "C:\Path\to\Extract.tde"

# Run Tableau extract
Start-Process -FilePath $TableauPath -ArgumentList "--tabcmd",
"export",
"$WorkbookPath",
"--fullpdf",
"--pagelayout",
"$ExtractPath",
"--timeout",
"600"
