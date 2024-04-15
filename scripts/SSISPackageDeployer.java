import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

public class SSISPackageDeployer {

    public static void main(String[] args) {
        String server = "0.tcp.eu.ngrok.io,10013";
        String database = "SSISDB";
        String username = "AutomationUser";
        String password = "Bow34908";

        String packageFilePath = "DatabaseAdministration/SSIS/ispac/GraduateMultiFile.ispac";
        Path path = Paths.get(packageFilePath);
        byte[] packageFileBytes = Files.readAllBytes(path);

        try {
            // Connect to SSMS
            Connection conn = DriverManager.getConnection(
                "jdbc:sqlserver://" + server + ";databaseName=" + database,
                username, password);

            // Deploy SSIS package
            Statement stmt = conn.createStatement();
            String sql = "DECLARE @folder_id uniqueidentifier = NULL;" +
                         "EXEC [catalog].[deploy_project] @folder_name=N'" + GraduateDB + "', @project_name=N'" + GraduateMultiFile+ "', " +
                         "@folder_id=@folder_id, @project_stream=0x" +
                         new String(packageFileBytes) +  // Replace with the binary stream of your .ispac file
                         "@operation_id=@operation_id OUTPUT, @operation_messages=@operation_messages OUTPUT";
            stmt.executeUpdate(sql);

            // Close resources
            stmt.close();
            conn.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
