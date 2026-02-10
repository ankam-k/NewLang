class Rec{
    public void printN(int n){
        if(n==1){
            System.out.println(n);
            return;
        }
        printN(n-1);
        System.out.println(n);
    }
    public void printRN(int n){
        if(n==1){
            System.out.println(n);
            return;
        }
        System.out.println(n);
        printRN(n-1);
    }
    public static void main(String[] args){
        Rec r=new Rec();
        System.out.println("Printing natural numbers: ");
        r.printN(5);
        System.out.println("Printing natural numbers in reverse order: ");
        r.printRN(5);
    }
}