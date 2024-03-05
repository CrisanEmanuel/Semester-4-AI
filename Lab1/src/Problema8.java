/*
Să se genereze toate numerele (în reprezentare binară) cuprinse între 1 și n. De ex. dacă n = 4,
 numerele sunt: 1, 10, 11, 100.
 */

import java.util.LinkedList;
import java.util.Queue;

public class Problema8 {

    /**
     * O(nlog n)
     * @param n numar natural
     * @return un string care contin numerele binare de la 1 la n
     */
    public static String generareBinar(int n) {
        StringBuilder numereBinare = new StringBuilder(" ");
        for (int i = 1; i <= n; i++) {
            String numarBinar = Integer.toBinaryString(i);
            numereBinare.append(numarBinar).append(" ");
        }
        return numereBinare.toString();
    }

    // solutie AI
    // O(n)
    // algoritm bazat pe BFS (Breadth-First Search) pe un graf binar
    // Vom crea un graf în care fiecare nod reprezintă un număr în reprezentare binară, iar muchiile reprezintă
    //trecerea de la un număr la altul prin adăugarea unui bit la finalul reprezentării binare. Vom începe de la
    //numărul 1 și vom explora succesiv toate posibilitățile adăugând câte un bit în fiecare pas. Vom opri
    //explorarea atunci când ajungem la numărul n.
    public static void generareBinarAI(int n) {
        Queue<String> queue = new LinkedList<>();
        queue.offer("1");

        for (int i = 0; i < n; i++) {
            String current = queue.poll();
            System.out.println(current);

            String next1 = current + "0";
            String next2 = current + "1";
            if (Integer.parseInt(next1, 2) <= n) {
                queue.offer(next1);
            }
            if (Integer.parseInt(next2, 2) <= n) {
                queue.offer(next2);
            }
        }
    }

    public static void run() {
        System.out.println("8) Numerele generate sunt: " + generareBinar(4));
        //System.out.println("8) Numerele generate sunt: ");
        //generareBinarAI(4);
    }
}
