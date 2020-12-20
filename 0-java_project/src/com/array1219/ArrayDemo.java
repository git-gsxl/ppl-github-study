package com.array1219;

/*
@USER PPL-泡泡龙 or 广深小龙
@date 2020-12-19 21:10
*/

import java.util.Scanner;

public class ArrayDemo {
    public static void main(String[] args) {
        // 定义初始值
        int[] numList = new int[5];
        int max = 0;

        // 实例化键盘输入类
        Scanner scan = new Scanner(System.in);

        System.out.println("请输入学生5个成绩");    // 打印键盘输入提示

        // 键盘输入值：循环 numList，共需要输入多少次，且判断最大值；
        for (int i = 0; i < numList.length; i++) {
            int num = scan.nextInt();
            numList[i] = num;
            if (numList[i] > max) {
                max = numList[i];
            }
        }

        // 再次遍历 numList ，根据 max 来进行分数评级；
        for (int i = 0; i < numList.length; i++) {
            if (numList[i] >= max - 10) {
                System.out.println("分数：" + numList[i] + " 等级为：A");
            } else if (numList[i] >= max - 20) {
                System.out.println("分数：" + numList[i] + " 等级为：B");
            } else if (numList[i] >= max - 30) {
                System.out.println("分数：" + numList[i] + " 等级为：C");
            } else {
                System.out.println("分数：" + numList[i] + " 等级为：D");
            }
        }
    }
}
