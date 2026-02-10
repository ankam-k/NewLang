import java.util.Scanner;
import java.util.Arrays;

class Array {
    public int[] input() {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter number of elements: ");
        int num = sc.nextInt();

        int[] numbers = new int[num];

        for (int i = 0; i < num; i++) {
            System.out.print("Enter number " + (i + 1) + ": ");
            numbers[i] = sc.nextInt();
        }
        return numbers; 
    }

    public int max(int[] numbers) {
        int maxVal = numbers[0];
        for (int i = 1; i < numbers.length; i++) {
            if (numbers[i] > maxVal) {
                maxVal = numbers[i];
            }
        }
        return maxVal;
    }

    public int min(int[] numbers) {
        int minVal = numbers[0];
        for (int i = 1; i < numbers.length; i++) {
            if (numbers[i] < minVal) {
                minVal = numbers[i];
            }
        }
        return minVal;
    }
    public static void main(String[] args) {
        Array array = new Array();
        int[] numbers = array.input(); 

        int max = array.max(numbers);
        int min = array.min(numbers);

        System.out.println("Maximum number is: " + max);
        System.out.println("Minimum number is: " + min);

        int[] arr1 = {1, 2, 3, 4, 5}; // sorted array
        int[] arr2 = {5, 3, 8, 2};    // unsorted array

        System.out.println(isSorted(arr1)); // true
        System.out.println(isSorted(arr2)); // false
    }

    public static boolean isSorted(int[] array) {
        for (int i = 0; i < array.length - 1; i++) {
            if (array[i] > array[i + 1]) {
                return false; 
            }
        }
        return true;
    }
}