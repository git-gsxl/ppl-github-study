package com.ppl.helloword.demo;

/*
@USER PPL-泡泡龙 or 广深小龙
@date 2020-12-06 16:06
*/

public class a_San {
    public static void main(String[] args) {
        // max：取最大值
        int a = 5;
        int b = 10;
        int max = (a > b) ? a : b;
        System.out.println(max);

        // 嵌套
        String maxStr = (a > b) ? "a大" : ((a == b) ? "ab相等" : "b大");
        System.out.println(maxStr);

        // 求三个数的最大值
        int c = 11;
        int maxSan = ((a > b) ? a : b) > c ? ((a > b) ? a : b) : c;
        System.out.println(maxSan);
    }
}
