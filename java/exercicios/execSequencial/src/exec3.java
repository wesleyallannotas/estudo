import java.util.Scanner;

public class exec3 {
    public static void main(String[] args) { 
        int a, b, c, d, resultado;
        Scanner sc = new Scanner(System.in);

        System.out.println("Digite quatro valores:");
        a = sc.nextInt();
        b = sc.nextInt();
        c = sc.nextInt();
        d = sc.nextInt();
        resultado = ((a * b) - (c * d));
        System.out.println("DIFERENCA =" + resultado);

        sc.close();
    }
}
