import java.util.Scanner;

public class JavaStaticInitializerBlock {

    public static int H;
    public static int B;
    public static boolean flag;
    static {
        try {
            Scanner scanner = new Scanner(System.in);
            H = scanner.nextInt();
            B = scanner.nextInt();
            if (H <= 0 || B <= 0) {
                flag = false;
                throw new Exception("Breadth and height must be positive");
            }
            else {
                flag = true;
            }
        }
        catch (Exception e){
            System.out.println(e);
        }
    }


    public static void  main(String[] args) {

        if(flag){
            int area=B*H;
            System.out.print(area);
        }

    }
}
