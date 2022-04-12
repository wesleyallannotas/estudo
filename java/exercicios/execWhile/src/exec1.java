import java.util.Scanner;

public class exec1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int senha;

        System.out.println("Digite a senha:");
        senha = sc.nextInt();

        while (senha != 2002) {
            System.out.println("Senha invalida, tente novamente:");
            senha = sc.nextInt();
        }
        
        System.out.println("Acesso permitido");
        sc.close();
    }
}
