package JavaPractice;
import java.util.Scanner;

public class ifelsejava {
    public static void main(String[] args) {
        int age;
        Scanner input = new Scanner(System.in);
        System.out.println("Enter Your Age: ");
        age = input.nextInt();
        if (age >= 18){
            System.out.println("You are eligible to vote.");
        }
        else{
            System.out.println("You are not eligible to vote.");
        }
    }
}
