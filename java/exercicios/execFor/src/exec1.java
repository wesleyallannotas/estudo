import java.util.Scanner;

public class exec1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int qt;

        System.out.println("Digite um numero inteiro:");
        qt = sc.nextInt();

        for (int i=0; i<=qt; i++) {
            if (i % 2 != 0) {
                System.out.println(i);
            }
        }
        System.out.println("Fim");
        sc.close();
    }
}
