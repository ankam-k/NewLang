import java.util.Scanner;

class Numbers {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter number of elements: ");
        int num = sc.nextInt();

        int[] numbers = new int[num];

        // Input elements
        for (int i = 0; i < num; i++) {
            System.out.print("Enter number " + (i) + ": ");
            numbers[i] = sc.nextInt();
        }

        // Ask for the number to search
        System.out.print("Enter the number to search for: ");
        int searchNumber = sc.nextInt();

        // Perform linear search
        boolean found = false;
        int position = -1;
        for (int i = 0; i < num; i++) {
            if (numbers[i] == searchNumber) {
                found = true;
                position = i;
                break;
            }
        }

        // Output result
        if (found) {
            System.out.println("Number found at position " + (position));
        } else {
            System.out.println("Number not found");
        }

        sc.close();
    }
}