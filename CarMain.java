class Car {

    // Attributes (Fields)
    String brand;
    String color;
    int speed;
    
    public Car(String brand, String color) {
        this.brand = brand;
        this.color = color;
        this.speed = 0; // default speed
    }

    public void displayInfo() {
        System.out.println("Brand: " + brand);
        System.out.println("Color: " + color);
        System.out.println("Speed: " + speed + " km/h");
    }

    public void accelerate(int increment) {
        speed += increment;
        System.out.println("Accelerated by " + increment + " km/h. Current speed: " + speed);
    }
}
public class CarMain {
    public static void main(String[] args) {
        Car myCar = new Car("Toyota", "Red");
        myCar.displayInfo();
        myCar.accelerate(30);
    }
}
