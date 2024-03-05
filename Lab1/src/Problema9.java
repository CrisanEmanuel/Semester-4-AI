/*
Considerându-se o matrice cu n x m elemente întregi și o listă cu perechi formate din coordonatele a 2 căsuțe din
matrice ((p,q) și (r,s)), să se calculeze suma elementelor din sub-matricile identificate de fiecare pereche.
De ex, pt matricea
[[0, 2, 5, 4, 1],
[4, 8, 2, 3, 7],
[6, 3, 4, 6, 2],
[7, 3, 1, 8, 3],
[1, 5, 7, 9, 4]]
și lista de perechi ((1, 1) și (3, 3)), ((2, 2) și (4, 4)), suma elementelor din prima sub-matrice este 38,
iar suma elementelor din a 2-a sub-matrice este 44
 */
/*
pairs = {{1, 1},
         {3, 3},
         {2, 2},
         {4, 4}};
 */
public class Problema9 {

    /**
     * O(n*m)
     * @param matrix matrice de dimensiune m x n
     * @param pairs matrice de perechi, prima pereche este reprezentata de primele 2 linii, a doua pereche de
     *              urmatoarele doua linii
     * @return String cu sumele partiale a sub-matricelor date de cele doua perechi
     */
    public static String sumePartiale(int[][] matrix, int[][] pairs) {
        int a1 = pairs[0][0], a2 = pairs[0][1];
        int b1 = pairs[1][0], b2 = pairs[1][1];
        int c1 = pairs[2][0], c2 = pairs[2][1];
        int d1 = pairs[3][0], d2 = pairs[3][1];
        int sumaPartiala1 = 0, sumaPartiala2 = 0;
        for (int i = a1; i <= b1; i ++) {
            for (int j = a2; j <= b2; j++) {
                sumaPartiala1 += matrix[i][j];
            }
        }
        for (int i = c1; i <= d1; i ++) {
            for (int j = c2; j <= d2; j++) {
                sumaPartiala2 += matrix[i][j];
            }
        }
        String suma1 = String.valueOf(sumaPartiala1);
        String suma2 = String.valueOf(sumaPartiala2);
        return "Prima suma este: " + suma1 + ", a doua suma este: " + suma2;
    }

    // solutie AI
    // mi-a dat cam aceeasi rezolvare
    public static void run() {
        System.out.println("9) " + sumePartiale(new int[][] {
                {0, 2, 5, 4, 1},
                {4, 8, 2, 3, 7},
                {6, 3, 4, 6, 2},
                {7, 3, 1, 8, 3},
                {1, 5, 7, 9, 4}}, new int[][] {{1, 1},
                                               {3, 3},
                                               {2, 2},
                                               {4, 4}}));
    }
}
