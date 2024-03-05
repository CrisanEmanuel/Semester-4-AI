/*
Să se determine al k-lea cel mai mare element al unui șir de numere cu n elemente (k < n).
De ex. al 2-lea cel mai mare element din șirul [7,4,6,3,9,1] este 7
 */

import java.util.Arrays;
import java.util.PriorityQueue;

public class Problema7 {

    /**
     * O(nlog k)
     * @param array vector de numere
     * @param k al catelea cel mai mare element
     * @return al k-lea cel mai mare element
     */
    public static int kCelMaiMare(int[] array, int k) {
        PriorityQueue<Integer> maxs = new PriorityQueue<>();

        for (int number : array) {
            maxs.add(number);
            if (maxs.size() > k) {
                maxs.poll();
            }
        }
        if (maxs.peek() != null) return maxs.peek();
        else return 0;
    }

    // solutie AI
    // O(nlog n)
    public static int kCelMaiMareAI(int[] array, int k) {
        Arrays.sort(array);
        return array[array.length - k];
    }


    public static void run() {
        System.out.println("7) Al 2-lea cel mai mare element este: " + kCelMaiMare( new int[] {7,4,6,3,9,1}, 2));
        //System.out.println("7) Al 2-lea cel mai mare element este: " + kCelMaiMareAI( new int[] {7,4,6,3,9,1}, 2));
    }
}
