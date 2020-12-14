package com.ppl.helloword.demo;

/*
@USER PPL-泡泡龙or广深小龙
@date 2020-12-13 22:11
*/

public class ForNew {
    public static void main(String[] args) {
        label:
        while (true) {
            labelFor:
            for (int i = 1; i < 1000; i++) {
                if (i == 8) {
                    System.out.println("结束循环：" + i);
                    break label;   // 结束外层(while)循环，否则会一直循环
                } else if (i == 6) {
                    System.out.println("continue：" + i);
                    continue labelFor;  // continue跳出本次for循环
                }
                System.out.println(i);
            }
        }
    }
}
