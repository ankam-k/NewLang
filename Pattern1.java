public class Pattern1 {
    public static void main(String[] args) {
        int n = 5;

       /*  for (int i = 1; i <= rows; i++) {
            for (int j = 1; j <= rows - i; j++) {
                System.out.print(" ");
            }
            for (int k = 1; k <= (2 * i - 1); k++) {
                System.out.print("*");
            }
            System.out.println();
        }

        for (int i = rows-1; i >= 1; i--) {
            for (int j = 1; j <= rows - i; j++) {
                System.out.print(" ");
            }
            for (int k = 1; k <= (2 * i - 1); k++) {
                System.out.print("*");
            }
            System.out.println();
        }

        System.out.println();System.out.println();
        for (int i = 1; i <= rows; i++) {
            for (int j = 1; j <= rows - i; j++) {
                System.out.print(" ");
            }
            for (int k = 1; k <= (2 * i - 1); k++) {
                System.out.print(i);
            }
            System.out.println();
        }

        System.out.println();System.out.println();
        for (int i = 1; i <= rows; i++){
            for(int j=1; j<=i; j++){
                System.out.print(i);   
            }
            System.out.println();
        }

        System.out.println();System.out.println();
        for (int i = 1; i <= rows; i++){
            for(int j=1; j<=i; j++){
                //System.out.print(j%2);   
                //System.out.println();
                System.out.print((i+j)%2);
            }
            System.out.println();
        }
        System.out.println();System.out.println();
        int n=5;
        int m=5;
        for (int i = 1; i <=n; i++) {
            for (int j = 1; j <=m; j++) {
                if (i==1 || j==1 || i==n || j==m){
                    System.out.print("* ");
                }
                else{
                    System.out.print("  ");
                }
            }
            System.out.println();
        }
        System.out.println();System.out.println();
        for (int i = 1; i <= n; i++) {
            // Print spaces for alignment
            for (int spaces = 1; spaces <= n - i; spaces++) {
                System.out.print(" ");
            }
            // Print increasing sequence
            for (int num = 1; num <= i; num++) {
                System.out.print(num);
            }
            // Print decreasing sequence
            for (int num = i - 1; num >= 1; num--) {
                System.out.print(num);
            }
            System.out.println(); // Move to next line
        }

        System.out.println();System.out.println();
        // Top half of the butterfly
        for (int i = 1; i <= n; i++) {
            // Left stars
            for (int j = 1; j <= i; j++) {
                System.out.print("* ");
            }
            // Spaces
            for (int j = 1; j <= 2 * (n - i); j++) {
                System.out.print("  ");
            }
            // Right stars
            for (int j = 1; j <= i; j++) {
                System.out.print("* ");
            }
            System.out.println();
        }

        // Bottom half of the butterfly
        for (int i = n-1; i >= 1; i--) {
            // Left stars
            for (int j = 1; j <= i; j++) {
                System.out.print("* ");
            }
            // Spaces
            for (int j = 1; j <= 2 * (n - i); j++) {
                System.out.print("  ");
            }
            // Right stars
            for (int j = 1; j <= i; j++) {
                System.out.print("* ");
            }
            System.out.println();
        }
        System.out.println();System.out.println();
        */
        
        // Top half of the butterfly
        for (int i = 1; i <= n; i++) {
            // Left side stars
            for (int j = 1; j <= i; j++) {
                if (j == 1 || j == i)
                    System.out.print("*");
                else
                    System.out.print(" ");
            }
            // Spaces in between
            for (int j = 1; j <= 2 * (n - i); j++) {
                System.out.print(" ");
            }
            // Right side stars
            for (int j = 1; j <= i; j++) {
                if (j == 1 || j == i)
                    System.out.print("*");
                else
                    System.out.print(" ");
            }
            System.out.println();
        }

        // Bottom half of the butterfly
        for (int i = n; i >= 1; i--) {
            // Left side stars
            for (int j = 1; j <= i; j++) {
                if (j == 1 || j == i)
                    System.out.print("*");
                else
                    System.out.print(" ");
            }
            // Spaces
            for (int j = 1; j <= 2 * (n - i); j++) {
                System.out.print(" ");
            }
            // Right side stars
            for (int j = 1; j <= i; j++) {
                if (j == 1 || j == i)
                    System.out.print("*");
                else
                    System.out.print(" ");
            }
            System.out.println();
        }
        System.out.println();System.out.println();
    }
}