package JavaPractice;

public class continuepracticejava {
    public static void main(String[] args) {
        /* 
        for(int j = 0; j<=5; j++){
            if (j==3){
                //continue;
                break;
            }
            System.out.println(j+" ");
        }
        */
        int counter = 0;
        while (counter<=5){
            if (counter == 3){
                counter++;
                //System.out.println("alarm ringing");
                continue;
            }
            System.out.println(counter);
            counter++;





            
        }

    }
}
