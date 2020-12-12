package com.ppl.helloword.demo;

/*
@USER PPL-泡泡龙 or 广深小龙
@date 2020-12-06 21:10
*/

import java.util.Scanner;

public class a_Scanner {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.println("请输入你的名字：");
        String name = scan.next();

        System.out.println("请输入你的年龄：");
        int age = scan.nextInt();

        System.out.println("请输入你的身高：");
        double height = scan.nextDouble();

        System.out.println("请输入你的体重：");
        short weight = scan.nextShort();

        System.out.println("你的名字为：" + name + "年龄为：" + age
                + "你的身高为：" + height + "你的体重为：" + weight);

//        int num = scan.nextInt();
//        System.out.println("数据处理后的值为：" + (num + 1));
    }
}
