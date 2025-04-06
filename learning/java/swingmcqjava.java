package JavaPractice;
import javax.swing.*;
import java.awt.event.*;



public class swingmcqjava {
    public static void main(String[] args) {
        JFrame window = new JFrame("mcq paper archive");

        
        JLabel q1 = new JLabel("What is 2+2");
        q1.setBounds(50,100,100,100);
        JRadioButton rb1 = new JRadioButton("2");
        rb1.setBounds(75,50,200,50);
        JRadioButton rb2 = new JRadioButton("8");
        rb2.setBounds(75,75,200,50);
        JRadioButton rb3 = new JRadioButton("12");
        rb3.setBounds(75,100,200,50);
        JRadioButton rb4 = new JRadioButton("4");
        rb4.setBounds(75,125,200,50);
        ButtonGroup bg1 = new ButtonGroup();
        bg1.add(rb1);
        bg1.add(rb2);
        bg1.add(rb3);
        bg1.add(rb4);


        JLabel q2 = new JLabel("What is 10+12");
        q1.setBounds(50,200,100,100);
        JRadioButton rb5 = new JRadioButton("A");
        rb5.setBounds(50,0,200,50);
        JRadioButton rb6 = new JRadioButton("B");
        rb6.setBounds(50,0,200,50);
        JRadioButton rb7 = new JRadioButton("C");
        rb7.setBounds(50,0,200,50);
        JRadioButton rb8 = new JRadioButton("D");
        rb8.setBounds(50,0,200,50);
        ButtonGroup bg2 = new ButtonGroup();
        bg2.add(rb5);
        bg2.add(rb6);
        bg2.add(rb7);
        bg2.add(rb8);


        JLabel q3 = new JLabel("");
        q1.setBounds(75,0,100,100);
        JRadioButton rb9 = new JRadioButton("A");
        rb9.setBounds(50,0,200,50);
        JRadioButton rb10 = new JRadioButton("B");
        rb10.setBounds(50,0,200,50);
        JRadioButton rb11 = new JRadioButton("C");
        rb11.setBounds(50,0,200,50);
        JRadioButton rb12 = new JRadioButton("D");
        rb12.setBounds(50,0,200,50);
        ButtonGroup bg3 = new ButtonGroup();
        bg3.add(rb9);
        bg3.add(rb10);
        bg3.add(rb11);
        bg3.add(rb12);


        window.add(rb1);
        window.add(rb2);
        window.add(rb3);
        window.add(rb4);
        window.add(rb5);
        window.add(rb6);
        window.add(rb7);
        window.add(rb8);
        window.add(rb9);
        window.add(rb10);
        window.add(rb11);
        window.add(rb12);
        window.add(q1);
        window.add(q2);
        window.add(q3);

        window.setSize(800,550);
        window.setLocation(100,100);
        window.setLayout(null);
        window.setVisible(true);
    }
}
