package com.ppl.helloword.demo;

/*
@USER PPL-泡泡龙 or 广深小龙
@date 2020-12-12 16:58
*/

import java.util.Scanner;

public class Test1212 {
    // 从键盘上输入2019年的"month”和"day"，要求通过程序输出输入的日期为2019年的第几天。
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("请输入月份");
        int moth = scan.nextInt();
        System.out.println("请输入日期");
        int day = scan.nextInt();
        int resDays = 0;

        switch (moth) {
            case 12:
                resDays += 30;
            case 11:
                resDays += 31;
            case 10:
                resDays += 30;
            case 9:
                resDays += 31;
            case 8:
                resDays += 31;
            case 7:
                resDays += 30;
            case 6:
                resDays += 31;
            case 5:
                resDays += 30;
            case 4:
                resDays += 31;
            case 3:
                resDays += 31;
            case 2:
                resDays += 28;
            case 1:
                resDays += day;
        }
        System.out.println(moth + "月" + day + "日" + "是当年的第 " + " " + resDays + "天");
    }
}
