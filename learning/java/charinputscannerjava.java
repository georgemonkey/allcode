package JavaPractice;
import java.util.Scanner;

public class charinputscannerjava {
    public static void main(String[] args) {
        char t1,t2;
        Scanner input = new Scanner(System.in);
        System.out.println("Enter The First Name: ");
        t1 = input.next().charAt(0);
       
        System.out.println("Enter The Last Name: ");
        t2 = input.next().charAt(0);
        input.close();
        
        
        System.out.println("The Initials Of The Name Is: " + t1+t2);
    }
}
