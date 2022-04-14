package application;

import java.util.Locale;
import java.util.Scanner;
import util.CurrencyConverter;

public class App {
    public static void main(String[] args) throws Exception {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        System.out.print("What is the dollar price? ");
        double cotacao = sc.nextDouble();
        System.out.print("How manu dollars will be bought? ");
        double dollars = sc.nextDouble();
        System.out.printf("Amount to be paid in reais = %.2f%n", CurrencyConverter.calc(cotacao, dollars)); 

        sc.close();
    }
}
