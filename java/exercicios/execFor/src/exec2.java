import java.util.Scanner;

public class exec2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int qt, x, in, out;
        in = 0;
        out = 0;

        System.out.println("Digite o numero de valor:");
        qt = sc.nextInt();
        
        for (int i=0; i<qt; i++) {
            x = sc.nextInt();
            if (x >= 10 && x <= 20) {
                in++;
            } else {
                out++;
            }
        }
        System.out.printf("%d in%n%d out%n", in, out);
        sc.close();
    }
}