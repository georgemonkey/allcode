package JavaPractice;
interface d{
    default void printd(){
        System.out.println("You are in Class D");
    }
}
interface e{
    default void printe(){
        System.out.println("You are in Class E");
    }
}


public class multipleinheritencejava implements d,e{
    public static void main(String[] args) {
        multipleinheritencejava obj = new multipleinheritencejava();
        obj.printd();
        obj.printe();
    }
}
