                  JAVA PRACTICALS 

Practical - 1: 

Aim: Static, Function overloading, Constructor overloading, function overriding 

Creating & calling (invoking) static method  

 

public class StaticTest { 

  // class method 

  static void myStaticMethod() { 

    System.out.println("Static methods can be called without creating objects"); 

  } 

 

  // instance method 

  public void myPublicMethod() { 

    System.out.println("Public methods must be called by creating objects"); 

  } 

 

  public static void main(String[ ] args) { 

       myStaticMethod(); // Call the static method 

    // myPublicMethod(); This would output an error 

 

    StaticTest obj = new StaticTest (); // Create an object of Main 

    obj.myPublicMethod(); // Call the public method 

  } 

} 

 

Design a class to overload a method volume( ) as follows: 

    double volume(double r) — with radius (r) as an argument, returns the volume of sphere using the formula: 
    v = (4/3) * (22/7) * r * r * r 

    double volume(double h, double r) — with height(h) and radius(r) as the arguments, returns the volume of a cylinder using the formula: 
    v = (22/7) * r * r * h 

    double volume(double 1, double b, double h) — with length(l), breadth(b) and height(h) as the arguments, returns the volume of a cuboid using the formula: 
    v = l*b*h ⇒ (length * breadth * height) 

 

public class Volume { 

double v; 

    double volume(double r) { 

         v = (4 / 3.0) * (22 / 7.0) * r * r * r; 

        return v; 

    } 

    double volume(double h, double r) { 

         v = (22 / 7.0) * r * r * h; 

        return v; 

    } 

      double volume(double l, double b, double h) { 

        v = l * b * h; 

        return v; 

      } 

    public static void main(String args[]) { 

        Volume obj = new Volume(); 

        System.out.println("Sphere Volume = " + obj.volume(6)); 

        System.out.println("Cylinder Volume = " + obj.volume(5, 3.5)); 

        System.out.println("Cuboid Volume = " +  obj.volume(7.5, 3.5, 2)); 

    } 

} 

 

Constructor overloading 

 

public class Main { 

 

  String language; 

 

  // constructor with no parameter 

  Main() { 

    this.language = "Java"; 

  } 

 

  // constructor with a single parameter 

  Main(String language) { 

    this.language = language; 

  } 

 

  public void getName() { 

    System.out.println("Programming Langauage: " + this.language); 

  } 

 

  public static void main(String[] args) { 

 

    // call constructor with no parameter 

    Main obj1 = new Main(); 

 

    // call constructor with a single parameter 

    Main obj2 = new Main("Python"); 

 

    obj1.getName(); 

    obj2.getName(); 

  } 

} 

 

Inheritance & method overriding  

class Animal { 

  public void animalSound() { 

    System.out.println("The animal makes a sound"); 

  } 

} 

 

class Pig extends Animal { 

  public void animalSound() { 

    System.out.println("The pig says: wee wee"); 

  } 

} 

 

class Dog extends Animal { 

  public void animalSound() { 

    System.out.println("The dog says: bow wow"); 

  } 

} 

public class OverloadTest { 

  public static void main(String[] args) { 

Pig obj1 = new Pig(); 

obj1.animalSound(); 

Dog obj2 = new Dog(); 

obj2.animalSound(); 

 

  } 

} 

 

 

 

Practical - 2: 

Aim: Write the four programs. in your notebook & bring completed notebook on practical day. 

Abstract class & abstract method  

abstract class GraphicObject { 

   int x, y; 

    void moveTo(int newX, int newY) { 

      x = newX; 

      y = newY; 

    } 

    abstract void draw(); 

    abstract void resize(); 

} 

 

class Circle extends GraphicObject { 

    //overriding draw & reshape method  

    public  void draw() { 

         System.out.println(“draw circle”); 

    } 

    public  void resize() { 

           System.out.println(“resize circle”); 

    } 

} 

 

class Rectangle extends GraphicObject { 

    //overriding draw & reshape method 

    public  void draw() { 

System.out.println(“draw rect”); 

    } 

    public  void resize() { 

System.out.println(“draw rect”); 

    } 

} 

 

class AbstracDemo { 

    public static void main(String[] args) { 

        Circle obj1 = new Circle (); 

obj1.draw(); 

obj1.resize(); 

        Rectangle  obj2 = new Rectangle  (); 

obj2.draw(); 

obj2.resize(); 

    } 

} 

================ 

 

Interface 

 

interface Animal { 

  //public static final field 

  int VAL = 20; 

   

  //public abstract  methods 

  void animalSound(); // interface method (does not have a body) 

  void sleep();  

} 

 

// Pig "implements" the Animal interface 

class Pig implements Animal { 

  //overriding animalSound & sleep method  

  public void animalSound() { 

    System.out.println("The pig says: wee wee"); 

  } 

  public void sleep() { 

    System.out.println("Zzz"); 

  } 

} 

 

public class InterfaceTest { 

  public static void main(String[] args) { 

    Pig myPig = new Pig();  // Create a Pig object 

    myPig.animalSound(); 

    myPig.sleep(); 

  } 

} 

======================= 

 

Inheriting two interfaces 

 

interface FirstInterface { 

  public void myMethod(); // interface method 

} 

 

interface SecondInterface { 

  public void myOtherMethod(); // interface method 

} 

 

class DemoClass implements FirstInterface, SecondInterface { 

//must give body to myMethod, myOtherMethod method  

  public void myMethod() { 

    System.out.println("Some text.."); 

  } 

  public void myOtherMethod() { 

    System.out.println("Some other text..."); 

  } 

} 

 

class Interface2Test { 

  public static void main(String[] args) { 

    DemoClass myObj = new DemoClass(); 

    myObj.myMethod(); 

    myObj.myOtherMethod(); 

  } 

} 

 

=============== 

 

User defined Exception 

 

class MyException extends Exception { 

private int detail; 

MyException(int a) { 

detail = a; 

} 

public String toString() { 

return "MyException[" + detail + "]"; 

} 

} 

 

class ExceptionDemo { 

 

static void compute(int a) throws MyException { 

System.out.println("Called compute(" + a + ")"); 

if(a > 10) 

throw new MyException(a); 

System.out.println("Normal exit"); 

} 

 

public static void main(String args[]) { 

try { 

compute(1); 

compute(20); 

} catch (MyException e) { 

System.out.println("Caught " + e); 

} 

finally { 

System.out.println("Finally block"); 

} 

} 

 

 

Practical – 3: 

Aim: Write the four programs. in your Sheet & bring completed one on practical day. 
COLLECTION FRAMEWORK 

 

ArrayList  

import java.util.*; 

class ArrayListDemo { 

    public static void main(String args[]) { 

// Create an array list. 

        ArrayList<String> al = new ArrayList<String>(); 

        System.out.println("Initial size of al: "+ al.size()); 

// Add elements to the array list. 

        al.add("C"); 

        al.add("A"); 

        al.add("E"); 

        al.add("B"); 

        al.add("D"); 

        al.add("F"); 

        al.add(1, "A2"); 

        System.out.println("Size of al after additions: " + al.size()); 

// Display the array list. 

        System.out.println("Contents of al: " + al); 

// Remove elements from the array list. 

        al.remove("F"); 

        al.remove(2);a 

        System.out.println("Size of al after deletions: "+ al.size()); 

         

        System.out.println("Contents of al: " + al); 

    } 

} 

 

Treeset 

 

import java.util.*; 

class HashSetDemo { 

public static void main(String args[]) { 

// Create a hash set. 

TreeSet<String> hs = new TreeSet<String>(); 

// Add elements to the hash set. 

hs.add("B"); hs.add("Af"); hs.add("Aa"); hs.add("D"); hs.add("C"); hs.add("F"); 

System.out.println(hs); 

    for(String s: hs) {  

        System.out.println(s); 

}  

} 

} 

 

Storing User-Defined Classes in Collections 

import java.util.*; 

class Address { 

private String name; 

private String street; 

private String city; 

private String state; 

private String code; 

Address(String n, String s, String c, 

String st, String cd) { 

name = n; 

street = s; 

city = c; 

state = st; 

code = cd; 

} 

public String toString() { 

return name + "\n" + street + "\n" + city + " " + state + " " + code; 

} 

} 

 

class MailList { 

          public static void main(String args[]) { 

LinkedList<Address> ml = new LinkedList<Address>(); 

// Add elements to the linked list. 

ml.add(new Address("J.W. West", "11 Oak Ave", "Urbana", "IL", "61801")); 

ml.add(new Address("Ralph Baker", "1142 Maple Lane", "Mahomet", "IL", "61853")); 

ml.add(new Address("Tom Carlton", "867 Elm St", "Champaign", "IL", "61820")); 

// Display the mailing list. 

for(Address element : ml) { 

System.out.println(element + "\n"); 

System.out.println();   } 

} 

} 

 

HashMap 

 

import java.util.*; 

class HashMapDemo { 

public static void main(String args[]) { 

// Create a hash map. 

HashMap<String, Double> hm = new HashMap<String, Double>(); 

 

// Put elements to the map 

hm.put("John Doe", new Double(3434.34)); 

hm.put("Tom Smith", new Double(123.22)); 

hm.put("Jane Baker", new Double(1378.00)); 

hm.put("Tod Hall", new Double(99.22)); 

hm.put("Ralph Smith", new Double(-19.08)); 

 

// Get a set of the entries. 

Set<Map.Entry<String, Double>> set = hm.entrySet(); 

 

// Display the set. 

for(Map.Entry<String, Double> me : set) { 

System.out.print(me.getKey() + ": "); 

System.out.println(me.getValue()); 

} 

System.out.println(); 

 

// Deposit 1000 into John Doe's account. 

double balance = hm.get("John Doe"); 

hm.put("John Doe", balance + 1000); 

 

System.out.println("John Doe's new balance: " + hm.get("John Doe")); 

} 

} 

 
 

Practical – 4: 

Aim: Swing 

 

Color Changer  JFrame with three JComboBox. 

import java.awt.*; 

import java.awt.event.*; 

import javax.swing.*; 

 

class ColorDemo implements ItemListener { 

    JComboBox<Integer> r,g,b; 

    JFrame jfrm ; 

    ColorDemo() { 

        jfrm = new JFrame("Color changer"); 

        jfrm.setSize(275, 100); 

        jfrm.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); 

 

        jfrm.setLayout(new FlowLayout()); 

        r = new JComboBox<>(); 

        g = new JComboBox<>(); 

        b = new JComboBox<>(); 

    

        jfrm.add(r); 

        jfrm.add(g); 

        jfrm.add(b); 

         

        for (int i = 0; i < 256; i++) { 

            r.addItem(i); 

            g.addItem(i); 

            b.addItem(i); 

        } 

         

        r.addItemListener(this); 

        g.addItemListener(this); 

        b.addItemListener(this); 

        // Display the frame. 

         jfrm.setVisible(true); 

    } 

    public static void main(String args[]) { 

       new ColorDemo(); 

    } 

 

    @Override 

    public void itemStateChanged(ItemEvent e) { 

        int rc= r.getSelectedIndex(); 

        int gc= g.getSelectedIndex(); 

        int bc= b.getSelectedIndex(); 

        System.out.println(rc +" "+ gc); 

        Color c = new Color (rc,gc,bc); 

        jfrm.getContentPane().setBackground(c); 

    } 

} 

 

Calculator  

import java.awt.*; 

import java.awt.event.*; 

import javax.swing.*; 

public class Calc extends JFrame implements ActionListener 

{ 

    public static void main(String args[]) { 

        new Calc(); 

    } 

    JButton add,sub,pro,div,clr; 

    JTextField t1,t2; 

    JLabel res; 

    public Calc() { 

        setTitle(" Calculator "); 

        add=new JButton("    +    "); 

        sub=new JButton("    -    "); 

        pro=new JButton("    *    "); 

        div=new JButton("    /    "); 

        clr=new JButton("  clear  "); 

        t1=new JTextField(20); 

        t2=new JTextField(20); 

        res=new JLabel(); 

        JPanel top=new JPanel(); 

        top.setBackground(Color.yellow); 

        JPanel bot=new JPanel(); 

        bot.setBackground(Color.blue); 

        bot.setLayout(new FlowLayout()); 

        bot.add(add); 

        bot.add(sub); 

 

        bot.add(pro); 

        bot.add(div); 

        bot.add(clr); 

        bot.add(res); 

        top.setLayout(new GridLayout(2,2)); 

        top.add(new JLabel("Number1:")); 

        top.add(t1); 

        top.add(new JLabel("Number2:")); 

        top.add(t2); 

        setLayout(new GridLayout(2,1)); 

        add(top); 

        add(bot); 

        setSize(400,150); 

        setVisible(true); 

        add.addActionListener(this); 

        sub.addActionListener(this); 

        pro.addActionListener(this); 

        div.addActionListener(this); 

        clr.addActionListener(this); 

        setDefaultCloseOperation(EXIT_ON_CLOSE); 

    } 

    public void actionPerformed(ActionEvent e) { 

        int n1= Integer.parseInt(t1.getText()); 

        int n2= Integer.parseInt(t2.getText()); 

        int r=0; 

        if(e.getSource()==add){ 

 

        r=n1+n2; 

        res.setText(r+""); 

        } 

        else if(e.getSource()==sub){ 

        r=n1-n2; 

        res.setText(r+""); 

        } 

        else if(e.getSource()==pro){ 

        r=n1*n2; 

        res.setText(r+""); 

        } 

        else if(e.getSource()==div){ 

        r=n1/n2; 

        res.setText(r+""); 

        } 

        else{ 

            t1.setText(""); 

            t2.setText(""); 

            res.setText(""); 

        } 

    } 

} 

 
 

Resume Builder 

 

import java.awt.*; 

import java.awt.event.*; 

import javax.swing.*; 

 

public class Resume extends JFrame implements ActionListener{ 

     public static void main(String args[]) { 

        new Resume(); 

    } 

      

    JButton sub,clr; 

    JTextField nm,bd,fn,nas,ph,em; 

    JRadioButton m, f; 

    JComboBox<String> q; 

     

    public Resume() {  

        setTitle("Resume builder");  

        setDefaultCloseOperation(EXIT_ON_CLOSE); 

        setLayout(new GridLayout(10,2)); 

        add(new JLabel("Student's Name")); 

        nm = new JTextField(25); 

        add(nm); 

        add(new JLabel("Father's Name")); 

        fn = new JTextField(25); 

        add(fn); 

        add(new JLabel("Birthday")); 

        bd = new JTextField(10); 

        add(bd); 

        add(new JLabel("Nationality")); 

        nas = new JTextField(25); 

        add(nas); 

        add(new JLabel("Phone ")); 

        ph = new JTextField(25); 

        add(ph); 

        add(new JLabel("E-Mail ")); 

        em = new JTextField(10); 

        add(em); 

        m = new JRadioButton("Male"); 

        f = new JRadioButton("Female"); 

        ButtonGroup bg = new ButtonGroup(); 

        //add(new JLabel("Gender ")); 

        bg.add(m); 

        bg.add(f); 

        add(m); 

        add(f); 

        add(new JLabel("Qualification")); 

        q= new JComboBox<>(); 

        q.addItem("A"); 

        q.addItem("B"); 

        q.addItem("C"); 

        add(q); 

        sub = new JButton("Submit"); 

        sub.addActionListener(this); 

        add(sub); 

        clr = new JButton("Clear"); 

        clr.addActionListener(this); 

        add(clr); 

        ta = new JTextArea(); 

        JScrollPane sp=new JScrollPane(ta, JScrollPane.VERTICAL_SCROLLBAR_AS_NEEDED,  

                JScrollPane.HORIZONTAL_SCROLLBAR_AS_NEEDED); 

        add(sp); 

        pack(); 

        setVisible(true); 

    } 

JTextArea ta; 

    @Override 

    public void actionPerformed(ActionEvent e) { 

        if (e.getSource()== sub) { 

            StringBuffer b = new StringBuffer(); 

            b.append(nm.getText() + '\n'); 

            b.append(fn.getText() + '\n'); 

            b.append(bd.getText() + '\n'); 

            b.append(nas.getText() + '\n'); 

            b.append(ph.getText() + '\n'); 

            b.append(em.getText() + '\n'); 

            b.append(bd.getText() + '\n'); 

            b.append(q.getSelectedItem() + "\n"); 

            ta.setText(b.toString()); 

        } 

        else { 

            nm.setText(""); 

            fn.setText(""); 

            bd.setText(""); 

            nas.setText(""); 

            ph.setText(""); 

            em.setText(""); 

            bd.setText(""); 

             

        } 

    } 

} 

 

Practical – 5: 

Aim: JDBC 

Create DataBase ‘mydb1’ in MySql 

Create table ‘emp’ with following fields & records. 

empid 
	

ename 
	

dept 
	

salary 

1 
	

Abc 
	

Sales 
	

100000 

2 
	

Xyz 
	

IT 
	

100000 

 

CREATE DATABASE mydb1; 

use mydb1; 

CREATE TABLE emp ( 

    empid int, 

    ename varchar(255), 

    dept varchar(255), 

    salary varchar(255) 

); 

INSERT INTO emp (empid, ename, dept, salary) 

values (1, ‘abc’, ‘sales’, ‘100000’); 

 

INSERT INTO emp (empid, ename, dept, salary) 

values (2, ‘xyz’, ‘IT’, ‘100000’); 

 

//prints all record of emp table present in mydb1 DB using executeQuery() 

import java.sql.*;   

class MysqlCon{   

public static void main(String args[]){   

try{   

    try{   

Class.forName("com.mysql.jdbc.Driver"); 

    }  

    }catch(ClassNotFoundException ce) { System.out.println(ce);}   

Connection con=DriverManager.getConnection(   

"jdbc:mysql://localhost:3306/mydb1","root","cs");   

Statement stmt=con.createStatement();   

ResultSet rs=stmt.executeQuery("select * from emp");   

while(rs.next())   

System.out.println(rs.getInt(1)+"  "+rs.getString(2)+"  "+ 

rs.getString(3) + rs.getInt(4);   

con.close();   

}catch(SqlException se) { System.out.println(se);}   

}   

}  

 

// inserting a record in emp table present in mydb1 DB using executeUpdate () 

import java.sql.*;   

class FetchRecord{   

public static void main(String args[])throws Exception{   

Class.forName("com.mysql.jdbc.Driver ");   

Connection con=DriverManager.getConnection("jdbc:mysql://localhost:3306/mydb1 ","root","cs");   

Statement stmt=con.createStatement();   

int result=stmt.executeUpdate("insert into emp values(3,'Irfan', ‘IT’ ,200000)");   

System.out.println(result+" records affected");   

con.close();   

} }   

// inserting values by user in emp table by using prepareStatement() 

import java.sql.*;   

class InsertPrepared{   

public static void main(String args[]){   

try{   

Class.forName("com.mysql.jdbc.Driver ");   

   

Connection con=DriverManager.getConnection("jdbc:mysql://localhost:3306/mydb1 ","root","cs");   

   

PreparedStatement stmt=con.prepareStatement("insert into emp values(?,?)");   

stmt.setInt(1,101);//1 specifies the first parameter in the query   

stmt.setString(2,"Ratan");   

   

int i=stmt.executeUpdate();   

System.out.println(i+" records inserted");   

   

con.close();   

  

}catch(Exception e){ System.out.println(e);}   

   

}   

}   

 

// GUI program to add record in table by using PreparedStatement  

import java.awt.*; 

import javax.swing.*; 

import java.awt.event.*; 

import java.sql.*; 

 

public class RecordAdd extends JFrame { 

    private JTextField name, eid, dept, salary; 

    private JButton add, exit; 

 

    public RecordAdd() { 

       addC(); 

 

        add.addActionListener(new ActionListener() { 

            public void actionPerformed(ActionEvent e) { 

                int id = Integer.parseInt(eid.getText()); 

     String n = name.getText(); 

     String d = dept.getText(); 

                int s = Integer.parseInt(salary.getText()); 

 

                try { 

                    Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/mydb1 ","root","cs"); 

                    PreparedStatement ps = con.prepareStatement( 

                    "INSERT INTO emp (empid, ename, dept, salary) VALUES (?, ?, ?, ?)"); 

                    ps.setInt(1, id); 

                    ps.setString(2, n); 

         ps.setString(3, d); 

         ps.setInt(4, s);         

                    int i= ps.executeUpdate(); 

if(i > 0) 

 JOptionPane.showMessageDialog(this,"Record added  successfully ");  

                    ps.close(); 

                    con.close(); 

                } catch (Exception ex) { 

                    ex.printStackTrace(); 

                } 

            } 

        }); 

       

    } 

    void addC(){ 

        setLayout(new GridLayout(5,5)); 

        add=new JButton("  Add  "); 

        add=new JButton("  Exit  "); 

        eid=new JTextField(20); 

        name=new JTextField(20); 

        dept=new JTextField(20); 

        salary=new JTextField(20); 

        

        add(new JLabel("  emp id  ")); 

        add(eid); 

        add(new JLabel("  name  ")); 

        add(name); 

        add(new JLabel("  department  ")); 

        add(dept); 

        add(new JLabel("  salary   ")); 

        add(salary); 

        add(add); 

        add(exit); 

        pack(); 

    } 

    public static void main(String[] args) {     

                new RecordAdd().setVisible(true); 

    } 

} 

 

JDBC-Swing (Modified) => Practical5 =>Q.4 
import java.awt.*; 
import javax.swing.*; 
import java.awt.event.*; 
import java.sql.*; 
 
public class RecordAdd extends JFrame implements ActionListener{ 
 
    private JTextField name, eid, dept, salary; 
    private JButton add, exit; 
 
    public RecordAdd() { 
        setLayout(new GridLayout(5, 2)); 
        add = new JButton("Add"); 
        exit = new JButton("Exit"); 
        eid = new JTextField(20); 
        name = new JTextField(20); 
        dept = new JTextField(20); 
        salary = new JTextField(20); 
        add(new JLabel(" emp id ")); 
        add(eid); 
        add(new JLabel(" name ")); 
        add(name); 
        add(new JLabel(" department ")); 
        add(dept); 
        add(new JLabel(" salary ")); 
        add(salary); 
        add(add); 
        add(exit);   
        add.addActionListener(this); 
        exit.addActionListener(this); 
        pack(); 
        
    } 
 
    public static void main(String[] args) { 
        new RecordAdd().setVisible(true); 
    } 
 
    @Override 
    public void actionPerformed(ActionEvent ae) { 
        if(ae.getActionCommand().equals("Add" )) { 
        int id = Integer.parseInt(eid.getText()); 
                String n = name.getText(); 
                String d = dept.getText(); 
                int s = Integer.parseInt(salary.getText()); 
                Connection con; 
                PreparedStatement ps; 
                try { 
                    con = DriverManager.getConnection("jdbc:mysql://localhost:3306/mydb1","root","cs"); 
                    ps = con.prepareStatement("INSERT INTO emp(empno, uname, dept, salary) VALUES( ?,  ?,  ?,  ?)"); 
                    ps.setInt(1, id); 
                    ps.setString(2, n); 
                    ps.setString(3, d); 
                    ps.setInt(4, s); 
                    int i = ps.executeUpdate(); 
                    if (i > 0) {                       
                    
                        JOptionPane.showMessageDialog(null, "Record added successfully"); 
                    } 
                    ps.close(); 
                    con.close(); 
                } catch (Exception ex) { 
                    ex.printStackTrace(); 
                } 
        } 
        else if (ae.getActionCommand().equals("Exit")) 
            System.exit(0); 
            } 
        } 

 

Practical – 6: 

Aim: Servlet 

Q.1) Servlet for checking user name and password from webpage. 

 

index.html 

---------- 

 

<!DOCTYPE html> 

<html> 

<head> 

<title>Authenticate user</title> 

</head> 

<body> 

<h1>Username:root,Password:root1</h1> 

<form action="NewServlet" method="post"> 

<input type="text" name="t1" size="20" placeholder="user name" /> <br> 

<input type="password" name="p1" size="20" placeholder="password" /><br> 

<input type="submit"> <input type="reset"> 

</form> 

</body> 

</html> 

 

Web.xml 

------- 

<?xml version="1.0" encoding="UTF-8"?> 

<web-app version="3.1" xmlns="http://xmlns.jcp.org/xml/ns/javaee" 

xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 

xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee 

http://xmlns.jcp.org/xml/ns/javaee/web-app_3_1.xsd"> 

<servlet> 

<servlet-name>NewServlet</servlet-name> 

<servlet-class>p1.NewServlet</servlet-class> 

 

</servlet> 

<servlet-mapping> 

<servlet-name>NewServlet</servlet-name> 

<url-pattern>/NewServlet</url-pattern> 

</servlet-mapping> 

<session-config> 

<session-timeout> 

30 

</session-timeout> 

</session-config> 

<welcome-file-list> 

<welcome-file>index.html</welcome-file> 

</welcome-file-list> 

</web-app> 

 

NewServlet.java 

--------------- 

package p1; 

 

import java.io.*; 

import javax.servlet.*; 

import javax.servlet.http.*; 

public class NewServlet extends HttpServlet { 

 

protected void processRequest(HttpServletRequest request, HttpServletResponse 

response, String m) throws ServletException, IOException { 

 

String s= request.getParameter("t1"); 

String p= request.getParameter("p1"); 

response.setContentType("text/html;charset=UTF-8"); 

 

try (PrintWriter out = response.getWriter()) { 

 

out.println("<!DOCTYPE html>"); 

out.println("<html>"); 

out.println("<head>"); 

out.println("<title>Servlet NewServlet</title>"); 

out.println("</head>"); 

out.println("<body>"); 

out.println("<h1> " + m + " Request</h1>"); 

if(s.equals("root") && p.equals("root1")) 

out.println("<h1>Welcome " + s + "</h1>"); 

else 

out.println("<h1>Hello</h1>"); 

out.println("</body>"); 

out.println("</html>"); 

} 

} 

@Override 

protected void doGet(HttpServletRequest request, HttpServletResponse 

response) 

throws ServletException, IOException { 

processRequest(request, response, "GET"); 

} 

@Override 

protected void doPost(HttpServletRequest request, HttpServletResponse 

response) 

throws ServletException, IOException { 

processRequest(request, response, "POST"); 

} 

} 

 

========================================================================= 

Q.2) Reading & writing cookies by using servlet 

 

index.html 

---------- 

<form action="servlet1" method="post">   

Name:<input type="text" name="userName"/><br/>   

<input type="submit" value="go"/>   

</form>   

 

FirstServlet.java 

----------------- 

import java.io.*;   

import javax.servlet.*;   

import javax.servlet.http.*;   

   

   

public class FirstServlet extends HttpServlet {   

   

  public void doPost(HttpServletRequest request, HttpServletResponse response){   

    try{   

   

    response.setContentType("text/html");   

    PrintWriter out = response.getWriter();   

           

    String n=request.getParameter("userName");   

    out.print("Welcome "+n);   

   

    Cookie ck=new Cookie("uname",n);//creating cookie object   

    response.addCookie(ck);//adding cookie in the response   

   

    //creating submit button   

    out.print("<form action='servlet2'>");   

    out.print("<input type='submit' value='go'>");   

    out.print("</form>");   

           

    out.close();   

   

        }catch(Exception e){System.out.println(e);}   

  }   

}  

 

SecondServlet.java 

------------------ 

import java.io.*;   

import javax.servlet.*;   

import javax.servlet.http.*;   

   

public class SecondServlet extends HttpServlet {   

   

public void doPost(HttpServletRequest request, HttpServletResponse response){   

    try{   

   

    response.setContentType("text/html");   

    PrintWriter out = response.getWriter();   

       

    Cookie ck[]=request.getCookies();   

    out.print("Hello "+ck[0].getValue());   

   

    out.close();   

   

         }catch(Exception e){System.out.println(e);}   

    }   

}  

 

web.xml 

------- 

<servlet>   

<servlet-name>s1</servlet-name>   

<servlet-class>FirstServlet</servlet-class>   

</servlet>   

   

<servlet-mapping>   

<servlet-name>s1</servlet-name>   

<url-pattern>/servlet1</url-pattern>   

</servlet-mapping>   

   

<servlet>   

<servlet-name>s2</servlet-name>   

<servlet-class>SecondServlet</servlet-class>   

</servlet>   

   

<servlet-mapping>   

<servlet-name>s2</servlet-name>   

<url-pattern>/servlet2</url-pattern>   

</servlet-mapping>     

 

Practical – 7: 

Aim: JSP 

1) Write a JSP that accepts a User Name from a HTML form and stores it as a cookie. Write another JSP that returns the value of this cookie and displays it 

 

index.html 

<html> 

   <body> 

<form action = "main.jsp" method = "GET"> 

         First Name: <input type = "text" name = "first"> 

         <br> 

         Last Name: <input type = "text" name = "last"> 

         <input type = "submit" value = "Submit"> 

      </form> 

       

   </body> 

</html> 

 

main.jsp 

<% 

   // Create cookies for first and last names.       

   Cookie firstName = new Cookie("first_name", request.getParameter("first")); 

   Cookie lastName = new Cookie("last_name", request.getParameter("last")); 

    

   // Set expiry date after 24 Hrs for both the cookies. 

   firstName.setMaxAge(60*60*24);  

   lastName.setMaxAge(60*60*24);  

    

   // Add both the cookies in the response header. 

   response.addCookie( firstName ); 

   response.addCookie( lastName ); 

%> 

 

<html> 

   <head> 

      <title>Setting Cookies</title> 

   </head> 

    

   <body> 

      <center> 

         <h1>Setting Cookies</h1> 

      </center> 

      <ul> 

         <li><p><b>First Name:</b> 

            <%= request.getParameter("first")%> 

         </p></li> 

         <li><p><b>Last  Name:</b> 

            <%= request.getParameter("last")%> 

         </p></li> 

      </ul> 

    

   </body> 

</html> 

 
 
 

Q.2) Write a JSP that displays the names and values of the cookie stored on the client. 

 

main.jsp 

<html> 

   <head> 

      <title>Reading Cookies</title> 

   </head> 

    

   <body> 

      <center> 

         <h1>Reading Cookies</h1> 

      </center> 

      <% 

         Cookie cookie = null; 

         Cookie[] cookies = null; 

          

         // Get an array of Cookies associated with the this domain 

         cookies = request.getCookies(); 

          

 

         if( cookies != null ) { 

            out.println("<h2> Found Cookies Name and Value</h2>"); 

             

            for (int i = 0; i < cookies.length; i++) { 

               cookie = cookies[i]; 

               out.print("Name : " + cookie.getName( ) + ",  "); 

               out.print("Value: " + cookie.getValue( )+" <br/>"); 

            } 

         } else { 

            out.println("<h2>No cookies founds</h2>"); 

         } 

      %> 

   </body>    

</html> 

 

Q.3) Write a JSP that accepts a User Name from a HTML form and stores it as a session variable. Write another JSP that returns the value of this session variable and displays it 

 

index.html 

<html>   

<body>   

<form action="welcome.jsp">   

<input type="text" name="uname">   

<input type="submit" value="go">   

</form>   

</body>   

</html>   

 
 
 

welcome.jsp 

<html>   

<body>   

<%    

   

String name=request.getParameter("uname");   

out.print("Welcome "+name);   

   

session.setAttribute("user",name);   

 

%>   

<a href="second.jsp">second jsp page</a>   

   

</body>   

 

second.jsp 

</html>   

 

<html>   

<body>   

<%    

   

String name=(String)session.getAttribute("user");   

out.print("Hello "+name);   

   

%>   

</body>   

</html>   

 

Practical – 8: 

Aim: JSP – JDBC 

Create table: 

============= 

Create table userlist (username varchar(20), password varchar(10)); 

 

Add records: 

============ 

INSERT INTO userlist(username, password) VALUES (“root”, “root”); 

INSERT INTO userlist(username, password) VALUES(“user”, “user”); 

 

 

1)Write a JSP code that accepts username and password from HTML file and validates the user from the database 

   

 

index.html 

========== 

<html> 

    <head> 

        <title>Welcome </title> 

    </head> 

    <body> 

        <form method = "post" action = "JspDB.jsp"> 

            <fieldset style="width:23%; background-color:#b3d1ff"> 

                <h3><center> Login Page</center></h3> 

                <hr> 

                <table> 

                    <tr> 

                        <td>Username:</td> 

                        <td> <input type = "text" name = "uname"></td> 

                    </tr> 

                    <tr> 

                        <td>Password:</td> 

                        <td><input type = "password" name = "pwd"></td> 

                    </tr> 

                    <tr> 

                        <td></td> 

                        <td><input type = "submit" value="check detail"></td> 

                    </tr> 

                </table> 

            </fieldset> 

        </form> 

    </body> 

</html> 

 

 

JspDB.jsp 

========= 

<%@ page import="java.sql.*"%> 

<%@ page import="java.util.*"%> 

<%! 

    Connection con; 

 

    PreparedStatement ps; 

    public void jspInit() 

    { 

        try 

        { 

            //loading the driver 

            Class.forName("com.mysql.jdbc.Driver"); 

            //establish the connection 

            con = DriverManager.getConnection("jdbc:mysql://localhost:3306/mydb", "root", "cs"); 

           //create statement object 

           // "select count(*) from userlist where username 

            ps = con.prepareStatement("select * from userlist where username = ? and password=?"); 

        } 

        catch(Exception ex) 

        { 

            ex.printStackTrace(); 

        } 

    } 

%> 

 

<%     

        //write jdbc code for authentication 

        String user = request.getParameter("uname"); 

        String pass = request.getParameter("pwd"); 

        //set form data as param value 

        ps.setString(1,user); 

        ps.setString(2,pass); 

        //excute the query 

        ResultSet rs = ps.executeQuery(); 

        int cnt = 0; 

        if (rs.next()) 

            cnt = rs.getInt(1); 

        if(cnt == 0) 

            out.println("<b><i><font color=red>Invalid credential</font></i></b>"); 

        else 

        { 

            out.println("<form><fieldset style= width:25%;>"); 

            out.println("<b><i><font color=red>valid credential..</font></i></b><br>"); 

            out.println("<b><i><font size=6 color=blue>Welcome to My Page</font></i></b>"); 

            out.println("</fieldset></form>"); 

        } 

    } 

%> 

<%! 

 

    public void jspDestroy() 

    { 

        try 

        { 

            //close 

            ps.close(); 

            con.close(); 

        } 

        catch(Exception ex) 

        { 

            ex.printStackTrace(); 

        } 

    } 

%> 

////////////////////////////////////////////////////////////////////////////////////////////////////////// 

 

 

2) Write a JSP that displays all the records of a table 

 

 

index.html 

========== 

<html> 

    <head> 

        <title>List all </title> 

    </head> 

    <body> 

        <form method = "post" action = "jsplist.jsp"> 

              <input type = "submit" value="check detail"> 

        </form> 

    </body> 

</html> 

 

 

jsplist.jsp 

========== 

<%@ page import="java.sql.*"%> 

<%@ page import="java.util.*"%> 

<%! 

    Connection con; 

    PreparedStatement ps; 

    public void jspInit() 

    { 

        try 

        { 

            //loading the driver 

            Class.forName("com.mysql.jdbc.Driver"); 

            //establish the connection 

            con = DriverManager.getConnection("jdbc:mysql://localhost:3306/mydb1", "root", "cs"); 

            //create statement object 

            ps2 = con.prepareStatement("select * from userlist"); 

        } 

        catch(Exception ex) 

        { 

            ex.printStackTrace(); 

        } 

    } 

%> 

<% 

        ResultSet rs = ps2.executeQuery(); 

        out.println("<table>"); 

        while(rs.next()) 

        { 

            out.println("<tr>"); 

            out.println("<td>"+rs.getString(1)+"</td>"); 

            out.println("<td>"+rs.getString(2)+"</td"); 

            out.println("</tr>"); 

        } 

        out.println("</table>"); 

        rs.close(); 

    }     

%> 

<%! 

    public void jspDestroy() 

    { 

        try 

        { 

            //close 

            ps.close(); 

            con.close(); 

        } 

        catch(Exception ex) 

        { 

            ex.printStackTrace(); 

        } 

    } 

%> 

 
