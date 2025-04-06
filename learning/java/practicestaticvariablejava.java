package JavaPractice;
class student{
    int rolenumber;
    String name;
    
    static String college = "abc college";
    static void college_display(){
        college = "def college";
    }
    student(int r, String n){
        rolenumber = r;
        name = n;
        
    }
void display(){
    System.out.println(rolenumber + " " + name + " " + college);
}
}
public class practicestaticvariablejava {
    public static void main(String[] args) {
        student s1 = new student(5, "raj");
        s1.display();
        student s2 = new student(7, "parth");
        student.college_display();
        s2.display();
    }
}
