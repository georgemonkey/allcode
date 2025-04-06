package JavaPractice;
import java.util.Scanner;

public class trafficsignal {
    public static void main(String[] args) {
        String option;
        Scanner input = new Scanner(System.in);
        System.out.println("Enter color of traffic signal(Red, Yellow and Green): " );
        option = input.nextLine();
        if (option.equals("green")){
            System.out.println("You should keep driving.");

        }
        else if (option.equals("yellow")){
            System.out.println("You should keep driving, but be careful while crossing the intersection.");

        }
        else if (option.equals("red")){
            System.out.println("You should stop the car at the intersection.");
        
        }
        else {
            System.out.println("The color signal is not recognized.");
        }
    }
    
}
