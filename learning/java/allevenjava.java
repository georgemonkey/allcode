package JavaPractice;
import java.util.Scanner;

public class allevenjava {
    public static void alleven(){
        Scanner input = new Scanner(System.in);
        System.out.println("Enter the minumun: ");
        int minn = input.nextInt();
        System.out.println("Enter the max: ");
        int maxn = input.nextInt();
        //int diff = maxn - minn;
        for (int i = minn; i<maxn; i++ ){
            //int diff2 = i%2;
            if (i%2==0){
                System.out.println(i);
            }
            
        }
     
    }
    public static void main(String[] args) {
        
        alleven();
    }
}