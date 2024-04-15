import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.Files;
import java.io.IOException;

public class SSISPackageDeployer {

    public static void main(String[] args) {
        String server = "0.tcp.eu.ngrok.io,10013";
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
                         new String(packageFileBytes) +  // Replace with the binary stream of your .ispac file
                         "@operation_id=@operation_id OUTPUT, @operation_messages=@operation_messages OUTPUT";
            stmt.executeUpdate(sql);

            // Close resources
            stmt.close();
            conn.close();
        } catch (SQLException | IOException e) {
            e.printStackTrace();
        }
    }
}
