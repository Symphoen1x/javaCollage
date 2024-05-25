public class Array {
    public static void main(String[] args) {
        // String[] anArray = { "S1", "S2", "S3" };
        // for (int i = 0; i < anArray.length; i++) {
        // System.out.println(anArray[i].toLowerCase());
        // }

        Object[] a = new Object[4];
        a[0] = new String("Hello, World");
        a[1] = new Long(44);
        a[2] = new Float(1.5);
        for (int i = 0; i < a.length; i++) {
            System.out.println("a[" + i + "] = " + a[i]);
        }

    }

}
