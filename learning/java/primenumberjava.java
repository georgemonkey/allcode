package JavaPractice;
import java.util.Scanner;
public class primenumberjava {
    public static void main(String[] args) {
        int i1;
        String s1;
        s1="f";
        Scanner input = new Scanner(System.in);
        System.out.println("Enter the number to check if it is prime or not.");
        i1= input.nextInt();
        for (int i=2; i<i1; i++){
            if (i1%i == 0){
                s1 = "t";
                break;
            }
            else{
                s1="f";
            }
        }     

        if (s1 == "t"){
                System.out.println("The number you provided is not a prime number.");
            }
            else{
                System.out.println("The number you provided is a prime number.");
            }


    }
}
