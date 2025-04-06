package JavaPractice;

public class operatorjava {
    public static void main(String[] args) {
        //1(Arithmetic)
        int num1 = 100, num2 = 20;
        System.out.println(num1+num2);
        System.out.println(num1-num2);
        System.out.println(num1*num2);
        System.out.println(num1/num2);
        System.out.println(num1%num2);
        //2(Assignment Operators)
        int num3 = 100, num4 = 50;
        num4 = num3;
        num4 += num3; //num4 = num4 + num3
        num4 -= num3;
        num4 *= num3;
        num4 /= num3;
        num4 %= num3;
        //3 Auto Increment / Decrement
        int num5 = 100, num6 = 50;
        num5++; //Num5 = Num5 + 1
        num6--; //Num6 = Num6 - 1
        //4(Logical Operators)
        boolean b1 = true;
        boolean b2 = false;
        System.out.println("b1 && b2: " + (b1 && b2));
        System.out.println("b1||b2: " + (b1 || b2));
        System.out.println("!(b1&&b2)" + (!(b1&&b2)));
        System.out.println("!(b1||b2)" + (!(b1||b2)));
        //5(Comparsion Or Relational)
        //>,<,>=.<=,==.!=
    }

}
