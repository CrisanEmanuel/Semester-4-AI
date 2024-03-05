import java.util.HashMap;
import java.util.Map;

/*
Pentru un șir cu n numere întregi care conține și duplicate, să se determine elementul majoritar (care apare de
mai mult de n / 2 ori). De ex. 2 este elementul majoritar în șirul [2,8,7,2,2,5,2,3,1,2,2].
 */
public class Problema6 {

    /**
     * O(n)
     * @param array un vector de numere intregi
     * @return elementul majoritar
     */
    public static int aparitii (int[] array) {
        int halfOfLength = array.length / 2;
        Map<Integer, Integer> freq = new HashMap<>();
        int maxim = 0;
        for (int number: array) {
            freq.put(number, freq.getOrDefault(number, 0) + 1);
            int aparitiiNumar = freq.get(number);
            if (aparitiiNumar >= halfOfLength && aparitiiNumar > maxim) {
                maxim = number;
            }
        }
        return maxim;
    }

    // solutie AI
    // algoritumul de votare Boyer-Moore
    // O(n)
    public static int aparitiiAI (int[] array) {
        int contor = 0;
        int max = 0;
        for(int number: array) {
            if (contor == 0) {
                max = number;
                contor = 1;
            } else if (number == max) {
                contor ++;
            } else {
                contor --;
            }
        }
        return max;
    }

    public static void run() {
        System.out.println("6) Elementul majoritar este: " + aparitii(new int[] {2,8,7,2,2,5,2,3,1,2,2}));
        //System.out.println("6) Elementul majoritar este: " + aparitiiAI(new int[] {2,8,7,2,2,5,2,3,1,2,2}));
    }
}
