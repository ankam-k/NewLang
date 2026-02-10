import java.util.Scanner;
class Power{
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        System.out.println("Enter a number to check if it is a power of 2:");
        int n=sc.nextInt();
        for(int i=0; i<n; i++){
            if(Math.pow(2,i)==n){
                System.out.println("2^" + i + " = " + Math.pow(2, i));
            } else {
                System.out.println("2^" + i + " is not equal to 10");
            }
        }
    }
}