package JavaPractice;

public class primenumberfunctionjava {
    public static void prime(int a) {
        String s1;
        s1="f";
        for (int i=2; i<a; i++ ){
            if (a%i ==0){
                s1="t";
                break;
            }
            else{
                s1="f";
            }
        }
        if (s1 == "t"){
            System.out.println(a+", The number you provided is not a prime number.");
        }
        else{
            System.out.println(a+", The number you provided is a prime number.");
        }
    }
    public static void main(String[] args) {
        prime(5);
    }

}
