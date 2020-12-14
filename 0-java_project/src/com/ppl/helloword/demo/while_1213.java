package com.ppl.helloword.demo;

/*
@USER PPL-泡泡龙or广深小龙
@date 2020-12-13 10:59
*/

import java.util.Scanner;

public class while_1213 {
    public static void main(String[] args) {
        // while
        int num = 0;
        while (num < 5) {
            num += 1;
            System.out.println("第几次了？" + num);
        }

        // do while
        int result = 0, a = 1;
        do {
            result += a;
            a++;
        } while (a < 5);
        System.out.println("result总和为：" + result);

        Scanner scan = new Scanner(System.in);
        while (true) {
            System.out.println("请输入数字：");
            double sendNum = scan.nextDouble();

            if (sendNum == 0) {
                System.out.println("结束");
                break;
            } else if (sendNum < 0) {
                System.out.println("负数");
            } else {
                System.out.println("正数");
            }
        }
    }
}
