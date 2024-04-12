# Variables
$SSISNamespace = "DatabaseAdministration/SSIS/Microsoft.SqlServer.Management.IntegrationServices.dll"
$TargetServerName = "0.tcp.eu.ngrok.io,10013"  # Update with your server name and port
$TargetDatabase = "GraduateDB"  # Update with your target database name
$TargetFolderName = "GraduateDB"
$ProjectFilePath = "DatabaseAdministration/SSIS/ispac/GraduateMultiFile.ispac"
$ProjectName = "GraduateMultiFile"
$Username = "AutomationUser"
$Password = "Bow34908"


# Create the SQL connection string with SQL Server Authentication
$sqlConnectionString = "Data Source=$TargetServerName;Initial Catalog=$TargetDatabase;User ID=$Username;Password=$Password;"
$sqlConnection = New-Object System.Data.SqlClient.SqlConnection $sqlConnectionString

# Load the IntegrationServices assembly
$loadStatus = [System.Reflection.Assembly]::Load("Microsoft.SQLServer.Management.IntegrationServices, "+
    "Version=16.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91, processorArchitecture=MSIL")

# Create a connection to the server
$sqlConnectionString = "Data Source=" + $TargetServerName + ";Initial Catalog=master;Integrated Security=SSPI;"
$sqlConnection = New-Object System.Data.SqlClient.SqlConnection $sqlConnectionString


# Create the Integration Services object
$integrationServices = New-Object $SSISNamespace".IntegrationServices" $sqlConnection

# Get the Integration Services catalog
$catalog = $integrationServices.Catalogs["SSISDB"]

# Create the target folder
$folder = New-Object $SSISNamespace".CatalogFolder" ($catalog, $TargetFolderName, "Folder description")
$folder.Create()

Write-Host "Deploying $ProjectName project ..."

# Read the project file and deploy it
[byte[]] $projectFile = [System.IO.File]::ReadAllBytes($ProjectFilePath)
$folder.DeployProject($ProjectName, $projectFile)

Write-Host "Done."


