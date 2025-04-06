package JavaPractice;

public class functionjava {
    public static void hypotenuse(double a, double b){
        double c = Math.sqrt(a*a+b+b);
        System.out.println(c);

    }
    public static void rarea(int l, int w) {
        int a = l*w;
        System.out.println("The area of the rectangle is: "+a);
        int p = l*2+w*2;
        System.out.println("The perimeter of the rectangle is: "+p);
        

    }
    public static double hypotenuse1(double pr, double bs){
        double h = Math.sqrt(pr*pr+bs*bs);
        return h;
    }
    public static void main(String[] args) {
        //hypotenuse(9, 5);
        //rarea(5, 3);
        double y=hypotenuse1(7, 5);
        System.out.println(y);
        System.out.println(hypotenuse1(7, 5)+hypotenuse1(1, 5));
        
    }
}
