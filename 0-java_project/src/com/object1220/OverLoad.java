package com.object1220;

/*
@USER PPL-泡泡龙 or 广深小龙
@date 2020-12-20 19:47
*/

public class OverLoad {

    // 方法重载，定义两个同名的方法：print
    public String print(String str) {
        return str;
    }

    public int print(int num) {
        return num;
    }
}

class OverLoadTest {
    public static void main(String[] args) {
        OverLoad o = new OverLoad();
        System.out.println(o.print("字符串"));
        System.out.println(o.print(666));
    }
}