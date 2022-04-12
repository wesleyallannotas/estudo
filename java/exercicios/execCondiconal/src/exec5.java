import java.util.Locale;
import java.util.Scanner;

public class exec5 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        int id, qt;
        double price = 0;
       
           System.out.println("Digite o ID do produto");
           id = sc.nextInt();
           System.out.println("Digite o Valor do produto");
           qt = sc.nextInt();

           if (id == 1) {
               price = qt * 4.0;
           } else if (id == 2) {
               price = qt * 4.5;
           } else if (id == 3) {
               price = qt * 5.0;
           } else if (id == 4) {
               price = qt * 2.0;
           } else if (id == 5) {
               price = qt * 1.5;
           }
           
           System.out.printf("Total: R$ %.2f%n", price);
    }
}