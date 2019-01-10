import java.util.Scanner;

public class JavaStringsIntroduction {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        String A = sc.next();
        String B = sc.next();

        System.out.println(A.length() + B.length());
        System.out.println(A.compareTo(B) > 0 ? "No" : "Yes");
        System.out.println(Character.toUpperCase(A.charAt(0)) + A.substring(1) + " " + Character.toUpperCase(B.charAt(0)) + B.substring(1));

    }
}
