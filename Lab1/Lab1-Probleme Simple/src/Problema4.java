/*
Să se determine cuvintele unui text care apar exact o singură dată în acel text. De ex. cuvintele care
apar o singură dată în ”ana are ana are mere rosii ana" sunt: 'mere' și 'rosii'.
 */

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class Problema4 {

    /**
     * O(n + m) pt ca face si split
     * @param text un text ce contine mai multe cuvinte separate prin spatiu
     * @return un string format din cuvintele ce apar o singura data in text
     */
    public static String cuvinte(String text) {
        StringBuilder cuvinteCareAparOData = new StringBuilder(" ");
        Map<String, Integer> freq = new HashMap<>();
        String[] cuvinte = text.split(" ");
        for (String cuv: cuvinte) {
            freq.put(cuv, freq.getOrDefault(cuv, 0) + 1);
        }

        for (Map.Entry<String, Integer> cuvant: freq.entrySet()) {
            if (cuvant.getValue() == 1) {
                cuvinteCareAparOData.append(cuvant.getKey()).append(" ");
            }
        }
        return cuvinteCareAparOData.toString();
    }

    // solutie AI
    // O(n)
    public static Set<String> cuvinteAI(String[] cuvinte) {
        // Inițializăm un HashSet pentru a stoca cuvintele care apar de mai multe ori
        Set<String> cuvinteMultiple = new HashSet<>();

        // Inițializăm un HashSet pentru a stoca cuvintele care apar o singură dată
        Set<String> cuvinteUnice = new HashSet<>();

        // Iterăm prin fiecare cuvânt din text
        for (String cuvant : cuvinte) {
            // Dacă cuvântul a fost deja adăugat în setul de cuvinte multiple,
            // îl adăugăm în setul de cuvinte unice
            if (!cuvinteMultiple.add(cuvant)) {
                cuvinteUnice.remove(cuvant);
            } else {
                // Dacă cuvântul nu a fost deja adăugat în setul de cuvinte unice,
                // îl adăugăm în setul de cuvinte unice
                cuvinteUnice.add(cuvant);
            }
        }
        return cuvinteUnice;
    }

    public static void run() {
        System.out.println("4) Cuvintele care apar o data sunt: " + cuvinte("ana are ana are mere rosii"));
        //System.out.println("4) Cuvintele care apar o data sunt: " + cuvinteAI(new String[] {"ana", "are", "ana", "are", "mere", "rosii"}));
    }
}
