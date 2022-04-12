import java.util.Locale;
import java.util.Scanner;

public class exec4 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        int id, horas;
        double salario, pago;

        System.out.println("Digite seu numero de identificação");
        id = sc.nextInt();
        System.out.println("Digite o numero de horas trabalhadas");
        horas = sc.nextInt();
        System.out.println("Digite o valor pago por hora");
        pago = sc.nextDouble();
        salario = (double) horas * pago;
        System.out.printf("Seu numero de identificação: %d%nSeu salario e: R$ %.2f%n", id, salario);

        sc.close();
    }
}