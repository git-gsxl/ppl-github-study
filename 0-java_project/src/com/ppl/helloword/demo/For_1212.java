package com.ppl.helloword.demo;

/*
@USER PPL-泡泡龙 or 广深小龙
@date 2020-12-12 21:51
*/

public class For_1212 {
    public static void main(String[] args) {
        int j_num = 0;
        int o_num = 0;
        int res_num = 0;
        int count = 1;
        int res = 0;
        for (int i = 1; i <= 100; i++) {
            if (i % 2 == 1) {
                j_num += i;
            } else {
                o_num += i;
            }
            res_num += i;
            if (i / 7 == count) {
                count += 1;
                res += i;
            }
        }
        System.out.println("1-100奇数总和为：" + j_num);
        System.out.println("1-100偶数总和为：" + o_num);
        System.out.println("1-100总和为：" + res_num);
        System.out.println("1-100是7的倍数的整数的个数：" + count);
        System.out.println("1-100是7的倍数的整数的总和：" + res);
        int age = 0;
        while (true) {
            age += 1;
            System.out.println(age);
            if (age == 3){
                System.out.println("break");
                break;
            }
        }
    }
}
