class Main {
    public void fillTheWaterBottle(boolean isBottleEmpty, boolean isBottleAvailable) {
        if (isBottleEmpty && isBottleAvailable) {
            System.out.println("Filling the water bottle...");
        } else {
            System.out.println("Not filling the bottle.");
        }
    }

    public static void main(String[] args) {
        Main obj = new Main();

        // Case 1: Bottle is empty and available
        boolean isBottleEmpty = true;
        boolean isBottleAvailable = true;
        obj.fillTheWaterBottle(isBottleEmpty, isBottleAvailable);

        // Case 2: Bottle is full or not available
        isBottleEmpty = false;
        isBottleAvailable = true;
        obj.fillTheWaterBottle(isBottleEmpty, isBottleAvailable);
    }
} 