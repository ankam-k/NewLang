public class TablesPrinter {

    public void printSingleTable(int number) {
        System.out.println("Table for " + number + ":");
        for (int j = 1; j <= 10; j++) {
            System.out.println(number + " x " + j + " = " + (number * j));
        }
        System.out.println();
    }
    public void printTables() {
        for (int i = 1; i <= 20; i++) {
            printSingleTable(i); 
        }
    } 
    public static void main(String[] args) {
        TablesPrinter printer = new TablesPrinter();
        printer.printTables();
    }
}