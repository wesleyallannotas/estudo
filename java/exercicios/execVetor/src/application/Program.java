package application;

import java.util.Scanner;

import entities.Client;

public class Program {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        Client[] vect = new Client[10];

        System.out.print("How many rooms will be rented? ");
        int n = sc.nextInt();
        
        for (int i=1; i<=n; i++) {
            System.out.println();
            System.out.println("Rent #" + i + ":");
            System.out.print("Name: ");
            sc.nextLine();
            String name = sc.nextLine();
            System.out.print("Email: ");
            String email = sc.nextLine();
            System.out.print("Room: ");
            int room = sc.nextInt();
            vect[room] = new Client(name, email);
            System.out.println();
        }
        
        System.out.println();
        System.out.println("Busy Rooms: ");
        for (int i=0; i<vect.length; i++) {
            if (vect[i] != null) {
                System.out.println(i + ": " + vect[i]);
            }
        }
        sc.close();
    }
}
