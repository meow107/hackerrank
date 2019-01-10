import java.time.format.DateTimeFormatter;
import java.util.Calendar;
import java.util.Scanner;

public class JavaDateandTime {

    public static String getDay(String day, String month, String year) {
        int iDay = Integer.parseInt(day);
        int iMonth = Integer.parseInt(month);
        int iYear = Integer.parseInt(year);

        Calendar cal = Calendar.getInstance();
        cal.set(Calendar.DAY_OF_MONTH, iDay);
        // with java 7 month begin with 0 not 1
        // interesting right?
        cal.set(Calendar.MONTH, iMonth - 1);
        cal.set(Calendar.YEAR, iYear);

        int dayOfWeek = cal.get(Calendar.DAY_OF_WEEK);
        switch (dayOfWeek) {
            case 1:
                return "SUNDAY";
            case 2:
                return "MONDAY";
            case 3:
                return "TUESDAY";
            case 4:
                return "WEDNESDAY";
            case 5:
                return "THURSDAY";
            case 6:
                return "FRIDAY";
            case 7:
                return "SATURDAY";
            default:
                return "";
        }
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String month = in.next();
        String day = in.next();
        String year = in.next();

        System.out.println(getDay(day, month, year));
    }

}
