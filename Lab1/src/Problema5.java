/*Pentru un șir cu n elemente care conține valori din mulțimea {1, 2, ..., n - 1} astfel încât o singură valoare se repetă de două ori,
să se identifice acea valoare care se repetă. De ex. în șirul [1,2,3,4,2] valoarea 2 apare de două ori.*/

import java.util.Arrays;
import java.util.HashSet;

public class Problema5 {
    /**
     * O(n)
     * @param vector vectorul de numere
     * @return vloarea care se repeta sau -1 daca nu exista
     */
    public static int seRepeta(int[] vector) {
        int i;
        int[] freq = new int[vector.length + 1];
        for (i = 0; i < vector.length; i++) {
            freq[vector[i]] ++;
            if (freq[vector[i]] > 1) {
                return vector[i];
            }
        }
        return -1;
    }


    /**
     * O(n)
     * @param vector vectorul de numere
     * @return vloarea care se repeta
     * Formula: sumaVector - len(vector)*(len(vector)-1)/2
     */
    public static int seRepetaAltaVarianta(int[] vector) {
        return Arrays.stream(vector).sum() - (vector.length * (vector.length - 1) / 2);
    }

    // solutie data de AI
    public static int seRepetaAI(int[] nums) {
        HashSet<Integer> set = new HashSet<>();

        for (int num : nums) {
            if (set.contains(num)) {
                return num;
            } else {
                set.add(num);
            }
        }
        return -1;
    }

    public static void run() {
        System.out.println("5) Valoarea care se repeta este: " + seRepeta(new int[] {1,2,3,4,2}));
        //System.out.println("5) Valoarea care se repeta este: " + seRepetaAltaVarianta(new int[] {1,2,3,4,2}));
        //System.out.println("5) Valoarea care se repeta este: " + seRepetaAI(new int[] {1,2,3,4,2}));
    }

}

