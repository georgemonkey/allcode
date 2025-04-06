package JavaPractice;

//0 1 1 2 3 5 8 13 21
public class fibbonaciseriesjava {
    public static void main(String[] args) {
        int terms = 8;
        int num1 = 0;
        int num2 = 1;
        int num3;
        System.out.print(num1+" "+num2);
        for (int i = 0; i<terms-2; i++){
            num3 = num1 + num2;
            System.out.print(" "+num3+" ");
            num1 = num2;
            num2 = num3;
            
        }
        
       
        
    }
    }
    


