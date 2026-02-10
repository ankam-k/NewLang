import java.util.Scanner;

class Bank {
    private String customerName;
    private String accountNumber;
    private double balance;

    public Bank(String customerName, String accountNumber, double initialBalance) {
        this.customerName = customerName;
        this.accountNumber = accountNumber;
        this.balance = initialBalance;
    }

    public void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
            System.out.println("Deposited: " + amount);
        } else {
            System.out.println("Invalid amount");
        }
    }

    public void withdraw(double amount) {
        if (amount > 0) {
            if (balance >= amount) {
                balance -= amount;
                System.out.println("Withdrawn: " + amount);
            } else {
                System.out.println("Insufficient balance");
            }
        } else {
            System.out.println("Invalid amount");
        }
    }

    public void checkBalance() {
        System.out.println("Current balance: " + balance);
    }

    public void enquires() {
        System.out.println("Customer Name: " + customerName);
        System.out.println("Account Number: " + accountNumber);
        System.out.println("Balance: " + balance);
        System.out.println("-------------------------");
    }
}

public class BankMain {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Bank[] accounts = new Bank[4];

        accounts[0] = new Bank("Alice", "A1001", 5000);
        accounts[1] = new Bank("Bob", "B2002", 10000);
        accounts[2] = new Bank("Charlie", "C3003", 7500);
        accounts[3] = new Bank("David", "D4004", 6000);

        System.out.println("Details of all bank accounts:");
        for (Bank account : accounts) {
            account.enquires();
        }
        sc.close();
    }
}