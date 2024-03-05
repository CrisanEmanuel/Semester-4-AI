/*Să se determine produsul scalar a doi vectori rari care conțin numere reale. Un vector este rar atunci
când conține multe elemente nule. Vectorii pot avea oricâte dimensiuni.
De ex. produsul scalar a 2 vectori unisimensionali [1,0,2,0,3] și [1,2,0,3,1] este 4.
 */
public class Problema3 {

    /**
     *
     * @param v1 primul vector de numere
     * @param v2 al doilea vector de numere
     * @return produs - produsul scalar a vectorilor v1 si v2
     */
    public static double produsScalar(double[] v1, double[] v2) {
        double produs = 0;
        int i = 0;
        while (i < v1.length) {
            produs += v1[i] * v2[i++];
        }
        return produs;
    }

    // solutie data de AI
    // e la fel, doar o formula de aplicat

    public static void run() {
        System.out.println("3) Produsul scalar este: " + produsScalar(new double[] {1,0,2,0,3}, new double[] {1,2,0,3,1}));
    }
}
