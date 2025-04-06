package JavaPractice;
import java.util.Scanner;

public class calculatorjava {
    public static void main(String[] args) {
        double n1;
        double n2;
        char o;
        double result;
        Scanner input = new Scanner(System.in);
        System.out.println("Enter your first number: ");
        n1 = input.nextDouble();
        System.out.println("Enter your second number: ");
        n2 = input.nextDouble();
        System.out.println("Enter the operation.(+, -, *, /): ");
        o = input.next().charAt(0);
        if (o == '+'){
            result = n1 + n2;
            System.out.println(result);
        }
        else if (o == '-'){
            result = n1 - n2;
            System.out.println(result);
        }
        else if (o == '*'){
            result = n1 * n2;
            System.out.println(result);
        }
        else if (o == '/'){
            result = n1 / n2;
            System.out.println(result);
        }
        

    }
    
}
