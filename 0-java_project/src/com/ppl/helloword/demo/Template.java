package com.ppl.helloword.demo;

/*
@USER PPL-泡泡龙 or 广深小龙
@date 2020-10-31 12:10
*/

import java.util.Arrays;

public class Template {

    // 模板一：psvm
    public static void main(String[] args) {
        int num = 1;

        // 模板二：sout
        System.out.println();
        // 变形：soutp、soutm、soutv、xxx.sout
        System.out.println("args = " + Arrays.deepToString(args));
        System.out.println("Template.main");
        System.out.println("args = " + args);
        System.out.println(num);

        // 模板三：fori
        for (int i = 0; i < num; i++) {
        }
        // 变形：xxx.fori

        // 模板四：ifn
/*        if (num == null) {
        }*/

}}
