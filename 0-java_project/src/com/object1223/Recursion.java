package com.object1223;

/*
@USER PPL-泡泡龙 or 广深小龙
@date 2020-12-23 22:13
*/

public class Recursion {
    public static void main(String[] args) {
        /*
        1、递归方法：一个方法内调用它自身(方法调方法)
        */
        Recursion rec = new Recursion();
        System.out.println(rec.getNumber(100));
    }

    // 计算1-100之间所有自然数之和;
    public int getNumber(int i) {
        if (i == 1) {
            return 1;
        } else {
            return i + getNumber(i - 1);
        }
    }
}
