package JavaPractice;

public class constructorpracticejava {
    int id;
    String name;
    constructorpracticejava(int a, String b){
        //System.out.println("constructor is created");
        id = a;
        name = b;
    }
    void display(){
        System.out.println(id+" "+name);
    }
    
    public static void main(String[] args) {
        constructorpracticejava obj1 = new constructorpracticejava(111,"Raj");
        constructorpracticejava obj2 = new constructorpracticejava(112, "Nikhil");
        obj1.display();
        obj2.display();
    }
}
