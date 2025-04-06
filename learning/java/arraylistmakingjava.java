package JavaPractice;
import java.util.ArrayList;

public class arraylistmakingjava {
    public static void main(String[] args) {
        ArrayList < String > car = new ArrayList<String>();
        car.add("Volvo");
        car.add("Mazda");
        car.add("Ford");
        car.add("Rivian");
        System.out.println(car);
        System.out.println(car.get(1));
        car.set(0,"Ferrari");
        System.out.println(car);
        car.set(3, "Honda");
        System.out.println(car);
    }
}
