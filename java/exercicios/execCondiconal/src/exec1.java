import java.util.Scanner;

public class exec1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x;

        System.out.println("Digite um valor inteiro:");
        x = sc.nextInt();

        if (x >= 0) {
            System.out.println("NAO NEGATIVO");
        } else {
            System.out.println("NEGATIVO");
        }

        sc.close();
    }
}
