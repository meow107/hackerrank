public class JavaMethodOverriding2 {
    public static void main(String []args) {
        MotorCycle M = new MotorCycle();
    }
}

class Bicycle {
    String defineMe() {
        return "a vehicle with pedals.";
    }
}

class MotorCycle extends Bicycle {
    String defineMe() {
        return "a vehicle with pedals.";
    }
    MotorCycle() {
        System.out.println("Hello I am a motorcycle, I am " + defineMe());
        String temp = super.defineMe();
        System.out.println("My ancestor is a cycle who is "+ temp);
    }
}
