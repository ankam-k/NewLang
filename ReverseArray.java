public class ReverseArray {
    public static void main(String[] args) {
        int[] array = {1, 2, 3, 4, 5};
        int start = 0;
        int end = array.length - 1;
        System.out.print("Original array: \n");
        for (int i = 0; i < array.length; i++) {
            System.out.print("Array element at index "+ i + " is "+array[i] + " ");
            System.out.println();
        }
        while (start < end) {
            int temp = array[start];
            array[start] = array[end];
            array[end] = temp;
            start++;
            end--;
        }
        System.out.print("Reversed array: \n");
        for (int i = 0; i < array.length; i++) {
            System.out.print("Array element at index "+ i + " is "+array[i] + " ");
            System.out.println();
        }
        System.out.println();
    }
}