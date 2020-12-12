package com.ppl.helloword.demo;

/*
@USER PPL-泡泡龙 or 广深小龙
@date 2020-12-05 22:18
*/

public class a_compare {
    public static void main(String[] args) {

        // 1、比较运算
        int a = 10;
        int b = 10;
        System.out.println(a == b);
        System.out.println(a != b);
        System.out.println(a >= b);
        System.out.println(a <= b);
        System.out.println(a < b);
        System.out.println(a > b);
        System.out.println(a = b);

        /*
        2、逻辑运算1
        且：&
        或：|
        非：!,取反
        异或：^
        */
        boolean i = true;
        boolean o = false;
        System.out.println(i & i);
        System.out.println(o | i);
        System.out.println(!o);       // 取反，原本o为false，取反变为true
        System.out.println(i ^ i);    // 异或，两值相同时为flase
        System.out.println(i ^ o);    // 异或，两值不相同时为true

        // 异或，类似且的取反，如下：
        System.out.println(!(i & i));
        System.out.println(!(i & o));

        /*
        2、逻辑运算2
        短路，且：&,值有一个为false，那全部为false，当值全为true时才为true
        短路，或：|,值有一个为true，那就为true，当值全为false时才为false
        */
        boolean aa = true;
        boolean bb = false;
        System.out.println(aa && bb);
        System.out.println(aa || aa);

        boolean x = true;
        boolean y = false;
        short z = 42;
        //if(y == true)
        if ((z++ == 42) && (y = true)) z++;
        if ((x = false) || (++z == 45)) z++;
        System.out.println("z=" + z);
    }
}
