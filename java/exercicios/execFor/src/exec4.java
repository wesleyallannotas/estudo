import java.util.Locale;
import java.util.Scanner;

public class exec4 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        
        int qt = sc.nextInt();

        for (int i=0; i<qt; i++) {
            int v1 = sc.nextInt();
            int v2 = sc.nextInt();

            if (v2 == 0) {
                System.out.println("Divisão Impossível");
            } else {
                double div = (double) v1 / v2;
                System.out.println(div);
            }
        }
        sc.close();
    }
}