package com.ppl.helloword.demo;

/*
@USER PPL-泡泡龙 or 广深小龙
@date 2020-12-11 22:24
*/

import java.util.Scanner;

public class Test1211 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("请输入您的身高：(cm)");
        int is_Gao = scan.nextInt();            // 身高
        System.out.println("请输入您的财富：(千万)");
        double is_money = scan.nextDouble();    // 财务
        System.out.println("请输入您是否帅：(是或否)");
        String is_Shu = scan.next();            // 是否帅

        if (is_Gao >= 180 && is_money >= 1 && is_Shu.equals("是")) {
            System.out.println("我一定要嫁给他");
        } else if (is_Gao >= 180 || is_money >= 1 || is_Shu.equals("是")) {
            System.out.println("比上不足，比下有余，还是嫁给他吧");
        } else {
            System.out.println("不用想了，不嫁");
        }
    }
}
