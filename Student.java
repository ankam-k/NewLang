public class Student {

    String name;
    int rollNo;
    int age;
    String course;
    double marks;

    void setDetails(String studentName, int studentRollNo, int studentAge, String studentCourse, double studentMarks) {
        name = studentName;
        rollNo = studentRollNo;
        age = studentAge;
        course = studentCourse;
        marks = studentMarks;
    }
 
    void displayInfo() {
        System.out.println("Name   : " + name);
        System.out.println("Roll No: " + rollNo);
        System.out.println("Age    : " + age);
        System.out.println("Course : " + course);
        System.out.println("Marks  : " + marks);
    }

    void updateMarks(double newMarks) {
        marks = newMarks;
        System.out.println("Marks updated to: " + marks);
    }

    void calculateGrade() {
        if (marks >= 90) {
            System.out.println("Grade: A");
        } else if (marks >= 75) {
            System.out.println("Grade: B");
        } else if (marks >= 60) {
            System.out.println("Grade: C");
        } else if (marks >= 35) {
            System.out.println("Grade: D");
        } else {
            System.out.println("Grade: F");
        }
    }

    void changeCourse(String newCourse) {
        course = newCourse;
        System.out.println("Course changed to: " + course);
    }
    public static void main(String[] args) {

        Student s1 = new Student();
        s1.setDetails("Kavya", 101, 20, "Computer Science", 80.0);
        s1.displayInfo();
        s1.updateMarks(90.5);
        s1.calculateGrade();
        s1.changeCourse("AI & ML\n");

        Student s2 = new Student();
        s2.setDetails("Keerti", 102, 20, "Web Development", 95.0);
        s2.displayInfo();
        s2.updateMarks(99.5);
        s2.calculateGrade();
        s2.changeCourse("Cloud Computing\n");

        Student s3 = new Student();
        s3.setDetails("Lahari", 103, 20, "Computer Science", 90.0);
        s3.displayInfo();
        s3.updateMarks(89.5);
        s3.calculateGrade();
        s3.changeCourse("Data Science\n");

        Student s4 = new Student();
        s4.setDetails("Vedhika", 104, 20, "AI & ML", 85.0);
        s4.displayInfo();
        s4.updateMarks(91.5);
        s4.calculateGrade();
        s4.changeCourse("Web Development\n");

        Student s5 = new Student();
        s5.setDetails("Abheesta", 105, 20, "Data Science", 85.0);
        s5.displayInfo();
        s5.updateMarks(97.5);
        s5.calculateGrade();
        s5.changeCourse("AI & ML\n");
    }
}
