/*
Considerându-se o matrice cu n x m elemente binare (0 sau 1) sortate crescător pe linii, să se identifice
indexul liniei care conține cele mai multe elemente de 1.
De ex. în matricea
[[0,0,0,1,1],
[0,1,1,1,1],
[0,0,1,1,1]]
a doua linie conține cele mai multe elemente 1.
 */
public class Problema10 {

    /**
     * O(n*m)
     * parcurg matricea pe coloane in jos, si la  primul 1 gasit returne indexul acelei linii deoarece numerele de pe
     * linii sunt ordonate crescator
     * @param matrix matrice de numere intregi
     * @return int indexul liniei cu cei mai multi de 1
     */
    public static int indexLine(int[][] matrix) {
        int numberRows = matrix.length;
        int numberCol = matrix[0].length;

        for (int i = 0; i < numberCol; i++) {
            int j = 0;
            while (j < numberRows) {
                if (matrix[j][i] == 1) return j;
                j++;
            }
        }
        return -1;
    }

    // solutie ai
    // elementele de pe fiecare linie fiind aranjate crescator, a facut cautare binara
    // O(nlog m)

    public static void run() {
        System.out.println("10) Indexul liniei este: " + indexLine(new int[][] {
                {0,0,0,1,1},
                {0,1,1,1,1},
                {0,0,1,1,1}}
        ));
    }
}
