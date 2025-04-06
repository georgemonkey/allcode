package JavaPractice;


public class abstaticcounterjava {
    static  int count = 0;
    abstaticcounterjava(){
        count++;
        System.out.println(count);
    }
    public static void main(String[] args) {
        abstaticcounterjava c5 = new abstaticcounterjava();
        abstaticcounterjava c1 = new abstaticcounterjava();
        abstaticcounterjava c2 = new abstaticcounterjava();
    }
    
}
