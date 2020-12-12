package com.ppl.helloword.demo;

/*
@USER PPL-泡泡龙 or 广深小龙
@date 2020-12-06 18:00
*/

public class IfTest {
    public static void main(String[] args) {
        int a = 1;
        int b = 2;
        // 第一种
        if (a < b) {
            System.out.println("a<b");
        }

        // 第二种
        if (a > b) {
            System.out.println("a>b");
        } else {
            System.out.println("a<b 且a!=b");
        }

        // 第三种
        if (a > b) {
            System.out.println("a>b");
        } else if (a == b) {
            System.out.println("a==b");
        } else {
            System.out.println("a<b 且a!=b");
        }

        // 交换值
        String s1 = "北京";
        String s2 = "南京";
        String s3;
        s3 = s1;
        s1 = s2;
        System.out.println(s1);
        System.out.println(s3);

        int num = 101;
        String str;
        if (num == 100) {
            str = "奖励：BMW";
        } else if (num > 80 && num <= 90) {
            str = "奖励：Iphone xs max";
        } else if (num > 60 && num <= 80) {
            str = "奖励：IPad";
        } else {
            str = "无奖励";
        }
        System.out.println(str);
    }
}
