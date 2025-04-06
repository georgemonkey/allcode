package JavaPractice;
import javax.swing.*;

import java.awt.Button;
import java.awt.event.*;


public class radiobuttonjava {
    public static void main(String[] args) {
        JFrame window = new JFrame("radiobuttonpractice");

        JRadioButton rb1 = new JRadioButton("Answer 1");
        rb1.setBounds(50,0,200,50);
        JRadioButton rb2 = new JRadioButton("Answer 2");
        rb2.setBounds(50,50,200,50);
        JRadioButton rb3 = new JRadioButton("Answer 3");
        rb3.setBounds(50,100,200,50);
        JRadioButton rb4 = new JRadioButton("Answer 4");
        rb4.setBounds(50,150,200,50);
        ButtonGroup bg1 = new ButtonGroup();
        bg1.add(rb1);
        bg1.add(rb2);
        bg1.add(rb3);
        bg1.add(rb4);

        JButton b1 = new JButton("Check Answers!");
        b1.setBounds(100,200,150,25);
        b1.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e){
                if (rb1.isSelected()){
                    JOptionPane.showMessageDialog(null,"You selected the correct option!");
                }
                else if (rb2.isSelected()){
                    JOptionPane.showMessageDialog(null,"You selected the correct option!");
                }
                else if (rb3.isSelected()){
                    JOptionPane.showMessageDialog(null,"You selected the correct option!");
                }
                else if (rb4.isSelected()){
                    JOptionPane.showMessageDialog(null,"You selected the correct option!");
                }
            }
        });


        window.add(rb1);
        window.add(rb2);
        window.add(rb3);
        window.add(rb4);
        window.add(b1);


        window.setSize(800,550);
        window.setLocation(100,100);
        window.setLayout(null);
        window.setVisible(true);

    }
}
