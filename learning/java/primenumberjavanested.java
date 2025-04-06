package JavaPractice;

public class primenumberjavanested {
    public static void main(String[] args) {
        int i1;
        String s1;
        s1="f";
        
        for (i1 = 3; i1 < 101;i1++){
        
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
                System.out.println(i1+" -The number you provided is not a prime number.");
            }
            else{
                System.out.println(i1+" -The number you provided is a prime number.");
            }
        }

    }
}
