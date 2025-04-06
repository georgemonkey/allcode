package JavaPractice;

public class whileloopprimenumbernestedjava {
    public static void main(String[] args) {
        int i1;
        String s1;
        s1="f";
        i1 = 3;
        while (i1<101){
            int i =2;
            while (i<i1){
                
                if (i1%i == 0){
                    s1 = "t";
                    break;
                }
                else{
                    s1="f";
                }
                i++;
              
            }
            
            if (s1 == "t"){
                System.out.println(i1+" -The number you provided is not a prime number.");
            }
            else{
                System.out.println(i1+" -The number you provided is a prime number.");
            }
            i1++;
        }

    
    }
}
