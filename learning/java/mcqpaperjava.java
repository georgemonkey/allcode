package JavaPractice;
import java.util.Scanner;

public class mcqpaperjava {
    static double score = 0;
    public static void mc(String question,String a, String b, String c, String d, String answer, int points){
        String option;
        System.out.println("-------------Question:-------------");
        System.out.println(question);
        System.out.println("-------------Options:-------------");
        System.out.println("The options are: ");
        System.out.println("a: "+a);
        System.out.println("b: "+b);
        System.out.println("c: "+c);
        System.out.println("d: "+d);
        
        Scanner input = new Scanner(System.in);
        
        
        option = input.nextLine();
        System.out.println("-------------Current Results:-------------");
        
        if (option.equals(answer)){
            System.out.println("Correct!");
            score += points;
            System.out.println("Current Score: " + score + "/" + "15");
            //System.out.println("Current Percentage: "+(score/15*100)+"%");
        }
        else {
            System.out.println("Incorrect :(");
            System.out.println("Current Score: " + score + "/" + "15");
            //System.out.println("Current Percentage: "+(score/15*100)+"%");
        }
    }
    public static void main(String[] args) {
        String username, password;
        Scanner input1 = new Scanner(System.in);
        System.out.println("Enter The Username: ");
        username = input1.nextLine();
        System.out.println("Enter The Password: ");
        password = input1.nextLine();
        if (username.equals("parth") && password.equals("123")){
            System.out.println("Login Succesful!");
            mc("who is awesome","Parth","Bob","Nikhil","Raj","a",5);
            mc("1+1= ","2","3","44","5","a",5);
            mc("3+3","7","9","11","10","b",5);
            System.out.println("Current Percentage: "+(score/15*100)+"%");
        }
        else{
            System.out.println("Login Failed");
        }
        
    }
}
