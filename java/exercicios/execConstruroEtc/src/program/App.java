package program;

import java.util.Locale;
import java.util.Scanner;

import entities.Account;

public class App {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        Account account;

        System.out.print("Enter account number: ");
        int idAccount = sc.nextInt();
        sc.nextLine();
        System.out.printf("Enter account holder: ");
        String name = sc.nextLine();
        System.out.print("Is there na initial deposit (y/n)?: ");
        char initial = sc.next().charAt(0);

        if(initial == 'y' || initial == 'Y') {
            System.out.print("Enter initial deposit: ");
            double initialDeposit = sc.nextDouble();            
            account = new Account(idAccount, name, initialDeposit);
        } else {
            account = new Account(idAccount, name);

        }

        System.out.println();
        System.out.println("Account Data:");
        System.out.println(account);

        System.out.print("Enter a deposit value: ");
        double depositValue = sc.nextDouble();
        account.deposit(depositValue);
        System.out.println("Updated Account Data:");
        System.out.println(account);
        
        System.out.print("Enter a withdraw value: ");
        double withdrawValue = sc.nextDouble();
        account.withdraw(withdrawValue);
        System.out.println("Updated Account Data:");
        System.out.println(account);

        
        sc.close();
    }
}
