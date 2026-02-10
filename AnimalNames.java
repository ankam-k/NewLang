import java.util.Scanner;

public class AnimalNames {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("How many animal names do you want to enter? ");
        int numAnimals = scanner.nextInt();
        scanner.nextLine(); 

        String[] animalNames = new String[numAnimals];

        for (int i = 0; i < numAnimals; i++) {
            System.out.print("Enter animal name " + (i + 1) + ": ");
            animalNames[i] = scanner.nextLine();
        }

        System.out.println("\nThe animal names you entered are:");
        for (String name : animalNames) {
            System.out.println(name);
        }

        scanner.close();
    }
}