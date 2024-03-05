/*Să se determine distanța Euclideană între două locații identificate prin perechi de numere.
De ex. distanța între (1,5) și (4,1) este 5.0
Dist = sqrt((x2-x1)^2 + (y2-y1)^2)
 */
public class Problema2 {
    /**
     * O(1)
     * @param x1 coordonata x a primului punct
     * @param y1 coordonata y a primului punct
     * @param x2 coordonata x a celui de-al doilea punct
     * @param y2 coordonata y a celui de-al doilea punct
     * @return distanta euclidiana dintre cele doua puncte
     */
    public static double distantaEuclidiana(double x1, double y1, double x2, double y2) {
        return Math.sqrt(Math.pow(x2-x1, 2) + Math.pow(y2-y1, 2));
    }

    // solutie data de AI
    // e la fel, e doar o formula de aplicat

    public static void run() {
        System.out.println("2) Distanta euclidiana este: " + distantaEuclidiana(1,5,4,1));
    }
}
