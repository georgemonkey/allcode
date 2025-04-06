package JavaPractice;

public class cuboidconstructorjava {
    int height;
    int width;
    int length;
    cuboidconstructorjava(int h,int w, int l){
        height = h;
        width = w;
        length = l;

    }
    void display(){
        //volume
        int volume = height*width*length;
        System.out.println("The volume of the cuboid is: " + volume);
        //surface area
        int SA = height*width+width*length+length*height;
        System.out.println("The surface area of the cuboid is: " + SA*2);
    }
    public static void main(String[] args) {
        cuboidconstructorjava obj1 = new cuboidconstructorjava(5, 5, 5);
        obj1.display();
    }
}
