package JavaPractice;
import javax.swing.*;
import java.awt.event.*;


public class mcqpaperRBjava {
    public static void main(String[] args) {
        JFrame window = new JFrame("parthy mcq paper");
        //GLOBAL VARS
        int w=200;
        int h=50;
        int x=25;
     
        //QUESTION ONE
        //question specfic vars
        int y1 = 0;
        //ui
        JLabel q1 = new JLabel("what is 2+2");
        q1.setBounds(x,y1,w,h);
        JRadioButton r1 = new JRadioButton("2");
        r1.setBounds(x,y1+25,w,h);
        JRadioButton r2 = new JRadioButton("4");
        r2.setBounds(x,y1+50,w,h);
        JRadioButton r3 = new JRadioButton("3");
        r3.setBounds(x,y1+75,w,h);
        JRadioButton r4 = new JRadioButton("5");
        r4.setBounds(x,y1+100,w,h);
        //element addition to the window
        window.add(q1);
        window.add(r1);
        window.add(r2);
        window.add(r3);
        window.add(r4);
        //radio button groups
        ButtonGroup bg1 = new ButtonGroup();
        bg1.add(r1);
        bg1.add(r2);
        bg1.add(r3);
        bg1.add(r4);
        

        //QUESTION TWO
        //question specfic vars
        int y2 = 150;
        //ui
        JLabel q2 = new JLabel("what is 2+8");
        q2.setBounds(x,y2,w,h);
        JRadioButton r5 = new JRadioButton("10");
        r5.setBounds(x,y2+25,w,h);
        JRadioButton r6 = new JRadioButton("9");
        r6.setBounds(x,y2+50,w,h);
        JRadioButton r7 = new JRadioButton("112");
        r7.setBounds(x,y2+75,w,h);
        JRadioButton r8 = new JRadioButton("11");
        r8.setBounds(x,y2+100,w,h);
        //element addition to the window
        window.add(q2);
        window.add(r5);
        window.add(r6);
        window.add(r7);
        window.add(r8);
        //radio button groups
        ButtonGroup bg2 = new ButtonGroup();
        bg2.add(r5);
        bg2.add(r6);
        bg2.add(r7);
        bg2.add(r8);

        //QUESTION THREE
        //question specfic vars
        int y3 = 300;
        //ui
        JLabel q3 = new JLabel("what is 10+12");
        q3.setBounds(x,y3,w,h);
        JRadioButton r9 = new JRadioButton("32");
        r9.setBounds(x,y3+25,w,h);
        JRadioButton r10 = new JRadioButton("28");
        r10.setBounds(x,y3+50,w,h);
        JRadioButton r11 = new JRadioButton("22");
        r11.setBounds(x,y3+75,w,h);
        JRadioButton r12 = new JRadioButton("16");
        r12.setBounds(x,y3+100,w,h);
        //element addition to the window
        window.add(q3);
        window.add(r9);
        window.add(r10);
        window.add(r11);
        window.add(r12);
        //radio button groups
        ButtonGroup bg3 = new ButtonGroup();
        bg3.add(r9);
        bg3.add(r10);
        bg3.add(r11);
        bg3.add(r12);

        //SUBMIT BUTTON
        JButton b1 = new JButton("Submit");
        b1.setBounds(200,500,100,50);
        window.add(b1);
        b1.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e){
                int score = 0;
                if (r2.isSelected()){
                    JOptionPane.showMessageDialog(null,"correct! Q1 score " + score);
                    score += 10; 
                }
                else{
                    JOptionPane.showMessageDialog(null,"incorrect:( Q1 score " + score);
                    score += 0;
                }
                if (r1.isSelected()){
                    JOptionPane.showMessageDialog(null,"correct! Q2 score " + score);
                    score += 10; 
                }
                else{
                    JOptionPane.showMessageDialog(null,"incorrect:( Q2 score " + score);
                    score += 0;
                }
                if (r3.isSelected()){
                    JOptionPane.showMessageDialog(null,"correct! Q3 score " + score);
                    score += 10; 
                }
                else{
                    JOptionPane.showMessageDialog(null,"incorrect:( Q3 score " + score);
                    score += 0;
                }
            }
        });

        //WINDOW MANAGEMENT
        window.setSize(800,600);
        window.setLocation(100,100);
        window.setLayout(null);
        window.setVisible(true);
    }
}
//JOptionPane.showMessageDialog(null,"correct");