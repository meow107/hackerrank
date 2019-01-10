import java.util.Scanner;

public class JavaLoops1 {

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int N = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");
        int i = 1;
        int busStop = 10;
        while (i <= busStop) {
            System.out.printf("%d x %d = %d\n", N, i, N * i);
            i ++;
        }

        scanner.close();
    }
}
