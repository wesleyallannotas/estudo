import java.util.Locale;
import java.util.Scanner;

public class exec2 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        double raio, pi, area;
        Scanner sc = new Scanner(System.in);
        
        pi = 3.14159;
        
        System.out.println("Informe o valor do raio");
        raio = sc.nextDouble();
        area = pi * Math.pow(raio, 2.0);
        System.out.printf("A area do circulo e: %.4f%n", area);

        sc.close();
    }
}
