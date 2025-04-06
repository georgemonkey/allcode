package JavaPractice;
import java.util.Scanner;

public class oddevenjava {
    public static void main(String[] args) {
        int n1;
        Scanner input = new Scanner(System.in);
        System.out.println("Enter a number: ");
        n1= input.nextInt();
        if (n1 % 2 == 0){
            System.out.println("The number you provided is an even number.");

        }
        else{
            System.out.println("The number you provided is an odd number.");
        }
    }
}
