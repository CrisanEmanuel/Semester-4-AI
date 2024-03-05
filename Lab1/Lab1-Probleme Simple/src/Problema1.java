/*
    Să se determine ultimul (din punct de vedere alfabetic) cuvânt care poate apărea într-un text care conține mai multe
cuvinte separate prin ” ” (spațiu).
    De ex. ultimul (dpdv alfabetic) cuvânt din ”Ana are mere rosii si galbene” este cuvântul "si".
 */

import java.util.Arrays;

public class Problema1 {

    /**
     * O(nlog n) face QuickSort
     * @param propozitie un array de cuvinte
     * @return ultimul cuvant dpdv alfabetic
     */
    public static String ultimCuvant(String propozitie) {

        String[] cuvinte = propozitie.split(" ");
        Arrays.sort(cuvinte);
        return cuvinte[cuvinte.length - 1];
    }

    // solutie AI
    // O(n)
    public static String ultimCuvantAI(String text) {
        String[] cuvinte = text.split(" ");
        String ultimulCuvant = cuvinte[0];

        for (String cuvant : cuvinte) {
            if (cuvant.compareTo(ultimulCuvant) > 0) {
                ultimulCuvant = cuvant;
            }
        }
        return ultimulCuvant;
    }

    public static void run() {
        System.out.println("1) Ultimul cuvant, alfabetic, este: " + ultimCuvant("Ana are mere rosii si galbene"));
        //System.out.println("1) Ultimul cuvant, alfabetic, este: " + ultimCuvantAI("Ana are mere rosii si galbene"));
    }
}
