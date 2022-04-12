import java.util.Locale;
import java.util.Scanner;

public class exec5 {
   public static void main(String[] args) {
    Locale.setDefault(Locale.US);
    Scanner sc = new Scanner(System.in);
    int id1, id2, qt1, qt2;
    double price1, price2, produto1, produto2, total;

    System.out.println("Informe ID, Valor Unitário e Quantidade");
    id1 = sc.nextInt();
    qt1 = sc.nextInt();
    price1 = sc.nextDouble();
    produto1 = qt1 * price1;

    System.out.println("Informe ID, Valor Unitário e Quantidade");
    id2 = sc.nextInt();
    qt2 = sc.nextInt();
    price2 = sc.nextDouble();
    produto2 = qt2 * price2;
    total = produto1 + produto2;
    
    System.out.printf("Valor a pagar: %.2f%n", total);

    sc.close();
   } 
}