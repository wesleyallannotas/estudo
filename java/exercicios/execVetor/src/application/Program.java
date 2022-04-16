package application;

import java.util.Locale;
import java.util.Scanner;

import entities.Client;

public class Program {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        System.out.print("How many rooms will be rented? ");
        int n = sc.nextInt();
        Client[] vect = new Client[9];
        int rent = 0;
        
        for (int i=0; i<n; i++) {
            sc.nextLine();
            rent++;
            System.out.println("Rent #" + rent);
            System.out.print("Name: ");
            String name = sc.nextLine();
            System.out.print("Email: ");
            String email = sc.nextLine();
            System.out.print("Room: ");
            int room = sc.nextInt();
            vect[room] = new Client(name, email);
            System.out.println();
        }
        
        for (int i=0; i<vect.length; i++) {
            if (vect[i] != null) {
                System.out.println(i + ": " + vect[i].getName() + ", " + vect[i].getEmail());
            }
        }

        sc.close();
    }
}
