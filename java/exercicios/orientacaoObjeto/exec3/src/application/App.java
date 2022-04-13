package application;

import java.util.Locale;
import java.util.Scanner;
import entities.Aluno;

public class App {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        Aluno aluno = new Aluno();

        System.out.print("Nome: ");
        aluno.name = sc.nextLine();
        System.out.print("Primeira Nota: ");
        aluno.nota1 = sc.nextDouble();
        System.out.print("Segunda Nota: ");
        aluno.nota2 = sc.nextDouble();
        System.out.print("Terceira Nota: ");
        aluno.nota3 = sc.nextDouble();
        System.out.printf("Nota Final = %.2f%n", aluno.notaFinal());
        System.out.println(aluno.notaCorte());


        sc.close();
    }
}