import java.util.Scanner;

public class exec4 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x, y, total;
        
        System.out.println("Digite a hora inicial e a hora final do");
        x = sc.nextInt();
        y = sc.nextInt();

        // if(x > y) {
        //     total = (Math.abs(x - 24) + y);
        // } else if (x < y) {
        //     total = y - x;
        // } else {
        //     total = 24;
        // }
        // System.out.printf("O jogo durou %d Hora(s)", total);

        if (x < y) {
            total = y - x;
        } else {
            total = 24 - x + y;
        }
        System.out.printf("O jogo durou %d Hora(s)", total);
        

        sc.close();
    }
}