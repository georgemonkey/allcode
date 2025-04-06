package JavaPractice;

public class constructorprimenumberjava {
    int i1;
    
   
    constructorprimenumberjava(int a){
        i1=a;
    }
        void prime(){
        String s1;
        s1 ="f";
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
            System.out.println(i1+": The number you provided is not a prime number.");
        }
        else{
            System.out.println(i1+": The number you provided is a prime number.");
        }
        }
    public static void main(String[] args) {
        constructorprimenumberjava obj1 = new constructorprimenumberjava(23);
        obj1.prime();
    }

}
