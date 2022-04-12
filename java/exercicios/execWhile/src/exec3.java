import java.util.Scanner;

public class exec3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int id, alc, gas, die;

        alc = 0;
        gas = 0;
        die = 0;
        id = 0;
        System.out.println("Digite o ID do combustível:");
        
        while (id != 4) {
        id = sc.nextInt();
            switch (id) {
                case 1:
                    alc++;
                    break;
                case 2:
                    gas++;
                    break;
                case 3:
                    die++;
                    break;
            }
        }
        System.out.printf("Muito Obrigado%nAlcool: %d%nGasolina: %d%nDiesel: %d%n", alc, gas, die);

        sc.close();
    }
}