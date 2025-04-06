package JavaPractice;

class teacher1 {
    String designation = "teacher";
    String college = "abc college";
    void does(){
        System.out.println("teaching");

    }
}
class student2 extends teacher1{
    String mainsubject = "math";
    void does2(){
        student2 obj = new student2();
        System.out.println(obj.designation);
        System.out.println(obj.college);
        System.out.println(obj.mainsubject);
    } 
}



public class multilevelnherintencejava extends student2{
    public static void main(String[] args) {
        multilevelnherintencejava obj2 = new multilevelnherintencejava();
        obj2.does();
        obj2.does2();
    }
}
