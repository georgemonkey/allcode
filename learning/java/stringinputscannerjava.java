package JavaPractice;
import java.util.Scanner;

public class stringinputscannerjava {
    public static void main(String[] args) {
        String t1,t2,output;
        Scanner input = new Scanner(System.in);
        System.out.println("Enter The First Name: ");
        t1 = input.nextLine();
       
        System.out.println("Enter The Last Name: ");
        t2 = input.nextLine();
        input.close();
        
        output = t1 + t2;
        System.out.println("The Full Name Is: " + output);
    }
}
