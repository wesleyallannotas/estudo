package app;

import java.util.Scanner;
import java.util.Locale;

import util.List;

public class Program {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        
        // Instanciação List
        List<Double> list = new List<>();

        // Menu
        int op;
        do {
            showMenu();
            op = sc.nextInt();
            switch (op) {
                case 1: {
                    System.out.print("Digite um numero: ");
                    double value = sc.nextDouble();
                    list.add(value);
                    break;
                }
                case 2: {
                    System.out.println(list.toString());
                    break;
                }
                case 3: {
                    System.out.println("Fim do programa");
                    break;
                }
                default: {
                    System.out.println("Opção invalida!");
                    break;
                }
            }
        }while (op != 3);
        // Encerra Scanner
        sc.close();
    }
    public static void showMenu() {
        System.out.println("1 - Inserir elemento da lista");
        System.out.println("2 - Mostra lista");
        System.out.println("3 - Sair");
    }
}