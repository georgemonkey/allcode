package JavaPractice;
import java.util.Scanner;
public class forloopjava {
    public static void main(String[] args) {
        //for(int i = 0; i < 10; i++ ){
            //System.out.println("Hi, There!");
            /* 
        int i1;
        Scanner input = new Scanner(System.in);
        System.out.println("Enter the table number you want: ");
        i1 = input.nextInt();
        int result;
        for (int i = 1; i < 13; i++){
            result = i1*i;
            System.out.println(i1 + " " + "* " + i + " = " + result);
            
            
        }
        */   
        int arr[] = {10,20,30,40,50};
        for (int num:arr){
            System.out.println(num);
        }
        String arr1[] = {"cookie","bear","rain"};
        for (String num1:arr1){
            System.out.println(num1);
        }
        int arr3[][] = {{1,2,3},{4,5,6}};
            for (int i=0; i<arr3.length;i++ ){
                for (int j = 0; j<arr3.length+1;j++){
                    System.out.println(arr3[i][j]);
                }
            }
        }
        
    }
   
