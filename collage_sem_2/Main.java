
public class Main {
    public static void main(String[] args) {   
        int[][] arrayOfints = {
            { 32, 87, 3, 589 },
            { 12, 1076, 2000, 8 },
            { 622, 127, 77, 955 }
        }; 
        boolean found = false;
        for (int i = 0; i < arrayOfints.length; i++) {
            for (int j = 0; j < arrayOfints[i].length; j++) {
                if (arrayOfints[i][j] == 12) {
                    System.out.println("Ditemukan 12 pada " + i + ", " + j);
                    found = true;
                    break;
                }
            }
            if (found) {
                break;
            }
        }

        if (!found) {
            System.out.println("Angka 12 tidak ditemukan dalam array.");
        }
    }
}


