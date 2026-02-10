import java.util.Scanner;

class Names {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter number of family members: ");
        int num = sc.nextInt();
        sc.nextLine(); // Consume leftover newline

        String[] names = new String[num];

        // Input family member names
        for (int i = 0; i < num; i++) {
            System.out.print("Enter name of family member " + (i + 1) + ": ");
            names[i] = sc.nextLine();
        }

        // Display all names
        System.out.println("\nFamily members are:");
        for (int i = 0; i < num; i++) {
            System.out.println("Family member " + (i + 1) + ": " + names[i]);
        }

        // Ask for the name to search
        System.out.print("\nEnter the name to search for: ");
        String searchName = sc.nextLine();

        // Perform linear search
        boolean found = false;
        int position = -1;
        for (int i = 0; i < num; i++) {
            if (names[i].equalsIgnoreCase(searchName)) {
                found = true;
                position = i;
                break;
            }
        }

        // Output the result
        if (found) {
            System.out.println(searchName + " found at position " + (position + 1));
        } else {
            System.out.println(searchName + " is not in the family list.");
        }

        sc.close();
    }
}