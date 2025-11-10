abstract class Shape {
    int a, b;
    abstract void printArea();
}

class Rectangle extends Shape {
    Rectangle(int x, int y) {
        a = x;
        b = y;
    }
    void printArea() {
        System.out.println("Area of Rectangle: " + (a * b));
    }
}

class Triangle extends Shape {
    Triangle(int x, int y) {
        a = x;
        b = y;
    }
    void printArea() {
        System.out.println("Area of Triangle: " + (0.5 * a * b));
    }
}

class Circle extends Shape {
    Circle(int r) {
        a = r;
    }
    void printArea() {
        System.out.println("Area of Circle: " + (3.14 * a * a));
    }
}

public class Main {
    public static void main(String[] args) {
        Shape r = new Rectangle(10, 5);
        Shape t = new Triangle(10, 5);
        Shape c = new Circle(7);

        r.printArea();
        t.printArea();
        c.printArea();
    }
}
