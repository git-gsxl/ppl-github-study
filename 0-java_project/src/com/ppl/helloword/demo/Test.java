package com.ppl.helloword.demo;

/*
@USER PPL-泡泡龙or广深小龙
@date 2020-12-13 17:59
*/

public class Test {
    public static void main(String[] args) {
        for (int i = 1; i < 1000; i++) {
            int resNum = 0;
            for (int j = 1; j < i; j++) {
                if (i % j == 0) {
                    resNum += j;
                }
            }
            if (i == resNum) {
                System.out.println(resNum);
            }
        }
    }
}
