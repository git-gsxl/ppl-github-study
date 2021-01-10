package com.interview;

/*
@USER PPL-泡泡龙 or 广深小龙
@date 2020-12-21 21:51
*/

public class Interview2 {
    public static void main(String[] args) {
        int a = 10;
        int b = 10;

        // 需要在method调用后仅打印出a=100,b=200；
        method(a, b);

        System.out.println("a=" + a);
        System.out.println("b=" + b);
    }

    public static void method(int a, int b) {
        a = a * 10;
        b = b * 20;
        System.out.println("a=" + a);
        System.out.println("b=" + b);
        System.exit(0);
    }
}
