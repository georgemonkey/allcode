package JavaPractice;
import java.util.Scanner;
public class digitevenjava {
   
        
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter the min number: ");
        int minn = input.nextInt();
        System.out.println("Enter the max: ");
        int maxn = input.nextInt();
        for (int i = minn; i<maxn; i++ ){
            
            if (i%2==0){
                int j = Math.floorDiv(i, 10);
                if (j%2==0){
                    int k = Math.floorDiv(j, 10);
                    if (k%2==0){
                        System.out.println(i);
                    }
                }

            }
            
            
        }
    
    }
}
//Plan A
//input min input max 
//check digits in number
//divide digits in number by 2 
//if remainder of all digits in number is zero then print the number

//Plan B
//input min input max
//divide complete number with 2
//if remainder = 0 divid number by 10
//remove the decimal part
//divide leftover number with 2
//if remainder = 0 divide number by 10
//remove the decimal part
//divide left number with 2
//if remainder = 0 print the entire number
//364