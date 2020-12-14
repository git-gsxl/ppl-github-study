package com.ppl.helloword.demo;

/*
@USER PPL-泡泡龙or广深小龙
@date 2020-12-13 11:29
*/

import java.util.Scanner;

public class HomeAccount {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int resMon = 0;     // 实际的钱
        String record = "";
        int record_id = 1;
        while (true) {
            System.out.println("--------家庭收支记账软件--------\n         1 收支明细\n         2 登记收入\n         3 登记支出\n         4 退出\n\n         ps: 使用功能请输入(1-4)：");
            int num = scan.nextInt();
            if (num == 1) {
                if (record == "") {
                    System.out.println("\n暂无记录~");
                    continue;
                } else {
                    System.out.println("\n收支明细如下：");
                    System.out.println(record);
                    continue;
                }
            } else if (num == 2) {
                System.out.println("\n登记收入功能");
                System.out.println("\n请输入本次需登记的金额：");
                int mon = scan.nextInt();
                if (mon <= 0) {
                    System.out.println("登记金额输入有误！\n");
                    continue;
                } else {
                    resMon += mon;
                    record += record_id + "：" + mon + "元\n";
                    record_id++;
                    System.out.println("本次钱结算剩余：" + resMon);
                }
            } else if (num == 3) {
                System.out.println("登记支出功能");
                System.out.println("请输入本次支出的金额：");
                int mon = scan.nextInt();
                if (mon >= 0) {
                    System.out.println("支出金额输入有误！\n");
                    continue;
                } else {
                    resMon += mon;
                    record += record_id + "：" + mon + "元\n";
                    record_id++;
                    System.out.println("本次钱结算剩余：" + resMon);
                }
            } else if (num == 4) {
                System.out.println("钱总剩余：" + resMon+"\n已退出~");
                break;
            } else {
                System.out.println("请输入(1-4)使用该功能");
            }
        }
    }
}
