package myServletPackages;

import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.IOException;
import java.io.PrintWriter;

@WebServlet("login-acc")
public class login extends HttpServlet {
    @Override
    public void doPost(HttpServletRequest req, HttpServletResponse res)
            throws IOException, ServletException {
        String name = req.getParameter("username");

        res.setContentType("text/html");
        PrintWriter out = res.getWriter();

        out.println("<h2>" + name + " </h2>");

    }

    public void destroy() {
        // do nothing.
    }
}
