import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.Files;
import java.io.IOException;

public class SSISPackageDeployer {
    private static final String TargetFolderName = "GraduateDB";
    private static final String ProjectName = "GraduateMultiFile";

    public static void main(String[] args) {
        String server = "0.tcp.eu.ngrok.io:10013";
        String database = "SSISDB";
        String username = "AutomationUser";
        String password = "Bow34908";
        String packageFilePath = "DatabaseAdministration/SSIS/ispac/GraduateMultiFile.ispac";

        try {
            // Connect to SSMS
            Connection conn = DriverManager.getConnection(
                "jdbc:sqlserver://" + server + ";databaseName=" + database,
                username, password);
            

            Path path = Paths.get(packageFilePath);
            byte[] packageFileBytes = Files.readAllBytes(path);

            // Deploy SSIS package
            Statement stmt = conn.createStatement();
            String sql = "DECLARE @folder_id uniqueidentifier = NULL;" +
                         "EXEC [catalog].[deploy_project] @folder_name=N'" + TargetFolderName + "', @project_name=N'" + ProjectName + "', " +
                         "@folder_id=@folder_id, @project_stream=0x" +
                         new String(packageFileBytes) + 
            stmt.close();
            conn.close();

        } catch (SQLException | IOException e) {
            e.printStackTrace();
        }
    }
}
