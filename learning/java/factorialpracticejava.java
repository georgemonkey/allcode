package JavaPractice;
import java.util.Scanner;


public class factorialpracticejava {

    public static void factorial(){
        int n1;
        int res;
        System.out.println("Enter an number: ");
        Scanner input = new Scanner(System.in);
        n1=input.nextInt();//n1 = 5
        int fact = 1;
        System.out.println("----------------------");
        for (int i = 1; i<=n1; i++){//i<=5, i=1, i=2, i=3, i=4, i=5
            fact = fact *i;//fact = 1*1 = 1, fact = 1*2 = 2, fact = 2*3 = 6, fact = 6*4 = 24, fact = 24*5 = 120
            System.out.println(fact);// 1, 2, 6, 24, 120

        }

    }
    public static void main(String[] args) {
        factorial();
    }
}
