import java.util.Scanner;

public class exec5 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int fatorial = 1;

        System.out.println("Digite um numero e descubra sua fatorial");
        int numero = sc.nextInt();
        
        for (int i=1; i<=numero; i++) {
            fatorial *= i;
        }
        
        System.out.println(fatorial);
        
        sc.close();
    }
}