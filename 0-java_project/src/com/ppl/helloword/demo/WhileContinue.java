package com.ppl.helloword.demo;

/*
@USER PPL-泡泡龙or广深小龙
@date 2020-12-13 11:19
*/

public class WhileContinue {
    public static void main(String[] args) {
        int result = 0;
        for (int i = 0; i <= 5; i++) {
            if (i == 3) {
                System.out.println(i);
                continue;
            }
            result += i;
        }
        System.out.println("result总和为：" + result);
    }
}