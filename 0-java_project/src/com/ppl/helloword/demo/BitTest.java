package com.ppl.helloword.demo;

/*
@USER PPL-泡泡龙 or 广深小龙
@date 2020-12-06 14:20
*/

public class BitTest {
    public static void main(String[] args) {
        int a = 2;
        int b = 8;
        //面试题:最高效方式的计算2* = 8,  2 << 3 或8 <<1
        // 相当于每向左移一位就 * 3
        System.out.println("a << 2 :" + (a << 3));

        // 相当于每向右移一位就 / 2
        System.out.println("a >> 2 :" + (b >> 2));

        int c = 12;
        int d = 5;
        System.out.println("c & d：" + (c & d));
        System.out.println("c & d：" + (c | d));
        System.out.println("c & d：" + (c ^ d));
    }
}
