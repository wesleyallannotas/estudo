package entities;

public class Rectangle {
    public double x;
    public double y;

    public double area() {
        return this.x * this.y;
    }
    public double perimeter() {
        return this.x * 2 + this.y * 2;
    }
    public double diagonal() {
        return  Math.sqrt(Math.pow(x, 2.0) + Math.pow(y, 2.0));
    }
}