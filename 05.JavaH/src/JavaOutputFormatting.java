import java.util.Scanner;

public class JavaOutputFormatting {

    // look https://gpcoder.com/2352-huong-dan-su-dung-string-format-trong-java/
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("================================");
        for (int i = 0; i < 3; i++) {
            String s1 = scanner.next();
            int x = scanner.nextInt();
            System.out.printf("%-15s%03d\n",s1,x);
        }
        System.out.println("================================");
    }
}
