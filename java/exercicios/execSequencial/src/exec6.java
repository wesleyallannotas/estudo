import java.util.Locale;
import java.util.Scanner;

public class exec6 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        double a, b, c, pi, cir, tri, trap, qua, ret;
        pi = 3.14159;

        System.out.println("Digite os valores:");
        a = sc.nextDouble();
        b = sc.nextDouble();
        c = sc.nextDouble();
        tri = a * c / 2;
        cir = pi * Math.pow(c, 2.0);
        trap = ((a + b) * c) / 2;
        qua = b * b;
        ret = a * b;
        System.out.printf("TRIANGULO: %.3f%nCIRCULO: %.3f%nTRAPZEIO: %.3f%nQUADRADO: %.3f%nRETANGULO: %.3f%n", tri, cir, trap, qua, ret);
        
        sc.close();
    }
}