import java.util.Locale;
import java.util.Scanner;

public class exec3 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        
        System.out.println("Numero de operações");
        int qt = sc.nextInt();
        for (int i=0; i<qt; i++) {
            double v1 = sc.nextDouble();
            double v2 = sc.nextDouble();
            double v3 = sc.nextDouble();
            double media = ((v1*2) + (v2*3) + (v3*5)) / 10;
            System.out.printf("%.1f%n", media);
        }
        sc.close();
    }
}