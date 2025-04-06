package JavaPractice;
import javax.swing.*;
import java.awt.event.*;
import java.util.ArrayList;



public class swingmcqfunctionjava {
    static JFrame window = new JFrame("mcq paper");
    public static void question(String question, String a1,String a2,String a3,String a4, String correctanswer,int a, int b, int c, int d){
        JLabel q1 = new JLabel(question);
        q1.setBounds(a,b,c,d);
        JRadioButton rb1 = new JRadioButton(a1);
        rb1.setBounds(a,b+25,c,d);
        JRadioButton rb2 = new JRadioButton(a2);
        rb2.setBounds(a,b+50,c,d);
        JRadioButton rb3 = new JRadioButton(a3);
        rb3.setBounds(a,b+75,c,d);
        JRadioButton rb4 = new JRadioButton(a4);
        rb4.setBounds(a,b+100,c,d);
        ButtonGroup bg1 = new ButtonGroup();
        bg1.add(rb1);
        bg1.add(rb2);
        bg1.add(rb3);
        bg1.add(rb4);
        JButton b1 = new JButton("Submit");
        b1.setBounds(a+200,b,100,50);
        
        b1.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e){
                if (rb1.isSelected()){
                    if (rb1.getActionCommand().equals(correctanswer)){
                        System.out.println("correct!");
                        int correct = 1;
                        
                    }
                    else {
                        System.out.println("incorrect:(");
                    }
                }
                else if (rb2.isSelected()){
                    if (rb2.getActionCommand().equals(correctanswer)){
                        System.out.println("correct!");
                        int correct = 2;
                    }
                    else {
                        System.out.println("incorrect:(");
                    }
                }
                else if (rb3.isSelected()){
                    if (rb3.getActionCommand().equals(correctanswer)){
                        System.out.println("correct!");
                        int correct = 3;
                    }
                    else {
                        System.out.println("incorrect:(");
                    }
                }
                else if (rb4.isSelected()){
                    if (rb4.getActionCommand().equals(correctanswer)){
                        System.out.println("correct!");
                    }
                    else {
                        System.out.println("incorrect:(");
                    }
                }
            }
        });
        window.add(rb1);
        window.add(rb2);
        window.add(rb3);
        window.add(rb4);
        window.add(q1);
        window.add(b1);
        
        
        
    }
    public static void main(String[] args) {
        
        question("what is 2+1","3","6","5","4","3",25,0,200,50);
        question("what is 2+2","9","100","30","4","4",25,150,200,50);
        question("what is 2+100","0","6","102","40","102",25,300,200,50);
    

        window.setSize(800,600);
        window.setLocation(100,100);
        window.setLayout(null);
        window.setVisible(true);
    }
}
