package JavaPractice;
import java.util.Scanner;
public class switchpracticejava {
    public static void main(String[] args) {
        int dayn;
        Scanner input = new Scanner(System.in);
        System.out.println("Enter the number of day.(Sunday = 0, Saturday = 6): ");
        dayn=input.nextInt();
        switch(dayn){
            case 0:
            System.out.println("Today is Sunday.");
            break;
            case 1:
            System.out.println("Today is Monday.");
            break;
            case 2:
            System.out.println("Today is Tuesday.");
            break;
            case 3:
            System.out.println("Today is Wensday.");
            break;
            case 4:
            System.out.println("Today is Thurday.");
            break;
            case 5:
            System.out.println("Today is Friday.");
            break;
            case 6:
            System.out.println("Today is Saturday.");
            break;
            default:
            System.out.println("Enter a valid day number.");
            break;
            
        }
    }   
}
