package JavaPractice;
import java.util.Scanner;

public class floatinputscannerjava {
    public static void main(String[] args) {
        float num1,num2,sum;
        Scanner input = new Scanner(System.in);
        System.out.println("enter the first number: ");
        num1 = input.nextFloat();
       
        System.out.println("enter the second number");
        num2 = input.nextFloat();
        input.close();
        
        sum = num1 + num2;
        System.out.println("The sum of " + num1 + " and " + num2 + " is " + sum);
    }
}
