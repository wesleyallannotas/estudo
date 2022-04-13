package application;

import java.util.Locale;
import java.util.Scanner;
import entities.Employee;

public class App {
    public static void main(String[] args) throws Exception {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        Employee employee = new Employee();
        
        System.out.print("Nome: ");
        employee.name = sc.nextLine();
        System.out.print("Salario Bruto: ");
        employee.grossSalary = sc.nextDouble();
        System.out.print("Taxa: ");
        employee.tax = sc.nextDouble();
        System.out.printf("Employee: %s, $ %.2f%n", employee.name, employee.netSalary());
        System.out.print("Porcentagem de aumento do salario: ");
        double porcentagem = sc.nextDouble();
        employee.increaseSalary(porcentagem);
        System.out.printf("Update Data: %s, $ %.2f%n", employee.name, employee.netSalary());

        sc.close();
    }
}
