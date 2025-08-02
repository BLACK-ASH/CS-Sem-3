import javax.swing.*;

public class demoButton {
    public static void main(String[] args) {
        JButton btn = new JButton("I Am Button.");
        btn.addActionListener(e-> System.out.println("I Am Clicked"));
        btn.setBounds(100,100,120,50);
        btn.setFocusable(false);

        JFrame frame = new JFrame();
        frame.setSize(400,400);
        frame.setVisible(true);
        frame.setLayout(null);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        frame.add(btn);
    }
}
