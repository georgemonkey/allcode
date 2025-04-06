package JavaPractice;
import java.util.Scanner;

public class doubleinputscannerjava {
    public static void main(String[] args) {
        double num1,num2,sum;
        Scanner input = new Scanner(System.in);
        System.out.println("enter the first number: ");
        num1 = input.nextDouble();
       
        System.out.println("enter the second number");
        num2 = input.nextDouble();
        input.close();
        
        sum = num1 + num2;
        System.out.println("The sum of " + num1 + " and " + num2 + " is " + sum);
    }
}
