import java.util.Scanner;

public class exec1 {
    public static void main(String[] args) throws Exception {
        int x, y, resultado;
        Scanner sc = new Scanner(System.in);

        System.out.println("Digite dos valores inteiros para serem somados");
        x = sc.nextInt();
        y = sc.nextInt();
        resultado = x + y;

        System.out.println("Resultado da soma: " + resultado);
        
        sc.close();
    }
}