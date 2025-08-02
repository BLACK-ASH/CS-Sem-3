import javax.swing.*;
import java.awt.*;

public class demoPanel {
    public static void main(String[] args) {
        JFrame frame = new JFrame();
        frame.setSize(300,300);
        frame.setLayout(null);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);

        JPanel redPanel = new JPanel();
        redPanel.setBounds(0,0,50,50);
        redPanel.setBackground(Color.red);
        frame.add(redPanel);

        JPanel greenPanel = new JPanel();
        greenPanel.setBounds(50,0,50,50);
        greenPanel.setBackground(Color.green);
        frame.add(greenPanel);

        JPanel bluePanel = new JPanel();
        bluePanel.setBounds(100,0,50,50);
        bluePanel.setBackground(Color.blue);
        frame.add(bluePanel);
    }
}
