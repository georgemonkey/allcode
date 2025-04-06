package JavaPractice;

public class stringmethodsjava {
    public static void main(String[] args) {
        String str = "parth";
        char chr = str.charAt(0);
        System.out.println(chr);
        int num1 =str.codePointAt(0);
        System.out.println(num1);
        String str1 = "Hello";
        String str2 = "fello";
        System.out.println(str1.compareTo(str2));
        System.out.println(str1.concat(str2));
        System.out.println(str1.length());
        System.out.println(str1.toLowerCase());
        System.out.println(str1.toUpperCase());
        char[] cs = {'h','e','l','l','o'};
        String s = new String(cs);
        System.out.println(s);
    }
}

