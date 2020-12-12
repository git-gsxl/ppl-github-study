package com.ppl.helloword.demo;

/*
@USER PPL-泡泡龙 or 广深小龙
@date 2020-11-29 17:03
*/

public class variable {
    public static void main(String[] args) {
        // 1、整数型

        // byte：1个字节=8bit，范围：-128 ~ 127
        byte byte_num = 127;
        System.out.println(byte_num);

        // short：2个字节，范围-2^15 ~ 2^15-1
        short short_num = 12777;
        System.out.println(short_num);

        // int：4个字节，范围约21亿
        // 常用int
        int int_num = 1875656565;
        System.out.println(int_num);

        // int：8个字节,常用大写L结尾
        // 声明long型常量须后加‘l’或‘L’
        long long_num = 18756565656L;
        System.out.println(long_num);
    }
}
