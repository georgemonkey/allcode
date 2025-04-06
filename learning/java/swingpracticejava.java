package JavaPractice;
import javax.swing.*;
import java.awt.event.*;

public class swingpracticejava {
   

        
    
    public static void main(String[] args) {
        
        
        JFrame window = new JFrame("parthprogram");
      
        JLabel l1 = new JLabel("User ID:");
        l1.setBounds(0,0,220,40);
        JTextField t1 = new JTextField();
        t1.setBounds(50,0,220,40);
       

        JLabel l2 = new JLabel("Password:");
        l2.setBounds(0,100,220,40);
        JPasswordField p1 = new JPasswordField();
        p1.setBounds(50,100,220,40);
        JButton b1 = new JButton("Login");
        b1.setBounds(100,150,220,40);
        b1.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e){
                String cpassword  = "1234";
                String pwd = new String(p1.getPassword());
        
                if (t1.getText().equals("parth") && pwd.equals(cpassword)){
                   
                    System.out.println("correct login");
                    JOptionPane.showMessageDialog(null,"Logged In!");
                    
        
                }
                else{
                    System.out.println("incorrect login");
                    JOptionPane.showMessageDialog(null,"Try Again!");
                }
            }
        });
        window.add(l1);
        window.add(t1);
        window.add(l2);
        window.add(p1);
        window.add(b1);

        window.setSize(400,250);
        window.setLocation(100,100);
        window.setLayout(null);
        window.setVisible(true);
      
       
        
    }
}

