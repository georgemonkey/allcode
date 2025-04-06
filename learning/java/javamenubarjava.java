package JavaPractice;
import javax.swing.*;
import java.awt.*;
public class javamenubarjava {
    public static void main(String[] args) {
        JFrame window = new JFrame("menubar");
        ImageIcon obj1 = new ImageIcon("/Users/parthamradkar/Library/Mobile Documents/com~apple~CloudDocs/Code/AllCode/CodeMedia/Icons/puffyfolder.png");
        Image obj2 = obj1.getImage();
        Image obj3 = obj2.getScaledInstance(25,25,java.awt.Image.SCALE_SMOOTH);
        ImageIcon obj4 = new ImageIcon(obj3);
        JMenuBar menubar =  new JMenuBar();

        JMenu menu1 = new JMenu("File");
        JMenuItem item1 = new JMenuItem("Open");
        item1.setIcon(obj4);
        menu1.add(item1);
        JMenuItem item2 = new JMenuItem("Save As");
        menu1.add(item2);
        JMenuItem item3 = new JMenuItem("Close");
        menu1.add(item3);
        menubar.add(menu1);
     
        JMenu menu2 = new JMenu("Edit");
        JMenuItem item4 = new JMenuItem("Undo");
        menu2.add(item4);
        JMenuItem item5 = new JMenuItem("Redo");
        menu2.add(item5);
        JMenuItem item6 = new JMenuItem("Cut");
        menu2.add(item6);
        menubar.add(menu2);
        
        
        window.add(menubar);
        window.setJMenuBar(menubar);



        window.setSize(400,500);
        window.setLocation(100,100);
        window.setLayout(null);
        window.setVisible(true);
    }
}
