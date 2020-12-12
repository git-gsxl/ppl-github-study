package com.ppl.helloword.demo;

/*
@USER PPL-泡泡龙 or 广深小龙
@date 2020-12-11 21:56
*/

public class dog {
    public static void main(String[] args) {
        int age = 2;
        if (age > 2) {
            System.out.println("相当于人的年龄：" + (2 * 10.5 + (age - 2) * 4));
        } else if (age > 0 && age <= 2) {
            System.out.println("相当于人的年龄：" + (age * 10.5));
        } else {
            System.out.println("狗的年龄有误，请重新输入");
        }
    }
}
