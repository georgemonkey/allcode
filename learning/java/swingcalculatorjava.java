package JavaPractice;
import javax.swing.*;
import java.awt.event.*;

public class swingcalculatorjava {
    public static void main(String[] args) {
        JFrame window = new JFrame("parthcalculator");

        JLabel title = new JLabel("Calculator");
        title.setBounds(90,5,220,40);
        JLabel l1 = new JLabel("First Number");
        l1.setBounds(10,40,150,30);
        JTextField firstnum = new JTextField();
        firstnum.setBounds(10,70,100,40);
        JLabel l2 = new JLabel("Second Number");
        l2.setBounds(10,120,150,30);
        JTextField secondnum = new JTextField();
        secondnum.setBounds(10,150,100,40);
        JTextField result = new JTextField();
        result.setBounds(25,250,200,40);


        JButton addb = new JButton("+");
        addb.setBounds(150,75,30,30);
        addb.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e){
               result.setText(Double.toString(Double.parseDouble(firstnum.getText())+Double.parseDouble(secondnum.getText())));
               firstnum.setText(null);
               secondnum.setText(null);
            }
        });
        JButton subtractb = new JButton("-");
        subtractb.setBounds(200,75,30,30);
        subtractb.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e){
               result.setText(Double.toString(Double.parseDouble(firstnum.getText())-Double.parseDouble(secondnum.getText())));
               firstnum.setText(null);
               secondnum.setText(null);
            }
        });
        JButton divideb = new JButton("/");
        divideb.setBounds(150,115,30,30);
        divideb.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e){
               result.setText(Double.toString(Double.parseDouble(firstnum.getText())/Double.parseDouble(secondnum.getText())));
               firstnum.setText(null);
               secondnum.setText(null);
            }
        });
        JButton multiplyb = new JButton("*");
        multiplyb.setBounds(200,115,30,30);
        multiplyb.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e){
               result.setText(Double.toString(Double.parseDouble(firstnum.getText())*Double.parseDouble(secondnum.getText())));
               firstnum.setText(null);
               secondnum.setText(null);
            }
        });



        window.add(title);
        window.add(l1);
        window.add(firstnum);
        window.add(l2);
        window.add(secondnum);
        window.add(addb);
        window.add(subtractb);
        window.add(divideb);
        window.add(multiplyb);
        window.add(result);

        window.setSize(250,400);
        window.setLocation(100,100);
        window.setLayout(null);
        window.setVisible(true);
    
    }
}
