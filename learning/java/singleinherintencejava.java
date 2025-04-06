package JavaPractice;

class teacher{
    String designation = "teacher";
    String college = "abc college";
    void does(){
        System.out.println("teaching");
    }
}

public class singleinherintencejava extends teacher{
    String mainsubject = "math";
    public static void main(String[] args) {
        singleinherintencejava obj1 = new singleinherintencejava();
        System.out.println(obj1.designation);
        System.out.println(obj1.college);
        System.out.println(obj1.mainsubject);
        obj1.does();  
    }
}
