package soma;

import java.util.Scanner;

public class somaJava {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    System.out.print("Digite um valor: ");
    int valor1 = sc.nextInt();
    System.out.print("Digite segundo valor: ");
    int valor2 = sc.nextInt();
    System.out.print("A valor da soma e " + soma(valor1, valor2));

    sc.close();
  }

  public static int soma(int valor1, int valor2) {
    return valor1 + valor2;
  }
}
