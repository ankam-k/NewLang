import java.util.Scanner;

// Class that performs operations
class Calculator {
    // Instance method to add three numbers
    public int addNumbers(int a, int b, int c) {
        return a + b + c;
    }

    // Instance method to subtract two numbers
    public int subtractNumbers(int a, int b) {
        return a - b;
    }
}

// Main class with main method
public class AdditionSubtraction {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the first number: ");
        int num1 = scanner.nextInt();

        System.out.print("Enter the second number: ");
        int num2 = scanner.nextInt();

        System.out.print("Enter the third number: ");
        int num3 = scanner.nextInt();

        // Create object of Calculator
        Calculator calculator = new Calculator();

        int sum = calculator.addNumbers(num1, num2, num3);
        int difference = calculator.subtractNumbers(num1, num2);

        System.out.println("Sum: " + sum);
        System.out.println("Difference: " + difference);

        scanner.close();
    }
}