import java.util.Scanner;

public class JavaLoops2 {

    public static void main(String []argh){
        Scanner in = new Scanner(System.in);
        int t=in.nextInt();
        for(int i=0;i<t;i++){
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();
            int count = 0;
            int sum = a;
            while (count < n) {
                sum = sum + b * (int)(Math.pow(2, count));
                System.out.printf("%d ",sum);
                count ++;
            }
            System.out.println();

        }
        in.close();
    }
}
