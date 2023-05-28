import java.io.DataInputStream;
import java.io.FileInputStream;
import java.util.ArrayList;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) {

    }

    private static int[] npiNumbers(){
        int[] npiNumbers = new int[]{
                1952305369,
                1871770255,
                1376710178,
                1598024044,
                1679527402,
                1689831323,
                1497296347,
                1447311915,
                1720620149,
                1346416997,
                1740366525,
                1427200716,
                1659469641,
                1477794584,
                1750654505,
                1003820630,
                1801450176,
                1497164354,
                1649356486,
                1336148345,
                1972762433,
                1760505481,
                1790931970,
                1548232465,
                1962858670,
                1821221805,
                1467611608,
                1023238979,
                1265503189,
                1861889834,
                1528145802,
                1225211469,
                1174528194,
                1619105475,
                1700270683,
                1881647980,
                1972508901,
                1912186875,
                1528007358,
                1790825081,
                1154734275,
                1952744898,
                1861758963,
                1437672623,
                1285926212,
                1780963660,
                1245328103,
                1023564234,
                1164789145,
                1114960523,
                1194801944,
                1992042527,
                1326043381,
                1922369669,
                1154720027,
                1003989625,
                1467538298,
                1619051265,
                1962518688,
                1245557891,
                1801005087,
                1336383967,
                1568429157,
                1982866463,
                1275503047,
                1144249541,
                1598977837,
                1679537476,
                1346874765,
                1679815260,
                1962723528,
                1154689867,
                1518361856,
                1629291612,
                1679515399,
                1063831006,
                1164584553,
                1316980428,
                1043868219,
                1114198751,
                1669454625,
                1649298977,
                1376791277,
                1396030680
        };
        return npiNumbers;
    }

    private static String[][] cmsDataSet(){
        String csvFile  = "CMSRefinedData.csv";
        String line;
        String csvSplitBy = ",";
        int numRows = 0;
        int numCols = 0;

        try (BufferedReader br = new BufferedReader(new FileReader(csvFile))) {
            // Count number of rows and columns in CSV file
            while ((line = br.readLine()) != null) {
                String[] values = line.split(csvSplitBy);
                numCols = Math.max(numCols, values.length);
                numRows++;
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        String[][] csvData = new String[numRows][numCols];

        try (BufferedReader br = new BufferedReader(new FileReader(csvFile))) {
            int row = 0;
            // Populate 2D array with CSV data
            while ((line = br.readLine()) != null) {
                String[] values = line.split(csvSplitBy);
                for (int col = 0; col < values.length; col++) {
                    csvData[row][col] = values[col];
                }
                row++;
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        return csvData;
    }

    private static String[][] cmsDataSelected(){
        int [] npiNumbers = npiNumbers();
        String[][] cmsDataSet = cmsDataSet();
        int i = 0;
        for (String npiNumber : cmsDataSet[1]){
            if (npiNumbers[i].equals(npiNumber)){
                
            }
        }


    }

}