import java.util.Scanner;

public class Tasks {
    public static void runAll() {
        Scanner scanner = new Scanner(System.in);
        int cmd;

        do {
        System.out.println(">>>");
        cmd = scanner.nextInt();

            switch (cmd) {
                case 1:
                    Problema1.run();
                    break;
                case 2:
                    Problema2.run();
                    break;
                case 3:
                    Problema3.run();
                    break;
                case 4:
                    Problema4.run();
                    break;
                case 5:
                    Problema5.run();
                    break;
                case 6:
                    Problema6.run();
                    break;
                case 7:
                    Problema7.run();
                    break;
                case 8:
                    Problema8.run();
                    break;
                case 9:
                    Problema9.run();
                    break;
                case 10:
                    Problema10.run();
                    break;
                case 0:
                    break;
                default:
                    System.out.println("Optiune invalida!");
            }
        } while(cmd != 0);

    }
}
