package app;

import java.util.Scanner;
import java.util.Locale;
import entities.Rectangle;

public class App {
    public static void main(String[] args) throws Exception {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        Rectangle rectangle = new Rectangle();
        
        System.out.print("Informe a largura do retângulo: ");
        rectangle.x = sc.nextDouble();
        System.out.print("Informe a altura do retângulo: ");
        rectangle.y = sc.nextDouble();
        System.out.printf("Area do Retângulo : %.2f%n", rectangle.area());
        System.out.printf("Perímetro do Retângulo: %.2f%n", rectangle.perimeter());
        System.out.printf("Diagonal do Retângulo: %.2f%n", rectangle.diagonal());

        sc.close();
    }
}
