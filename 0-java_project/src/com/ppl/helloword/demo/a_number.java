package com.ppl.helloword.demo;

/*
@USER PPL-泡泡龙 or 广深小龙
@date 2020-11-30 22:22
*/

public class a_number {
    public static void main(String[] args) {
        int a = 2;
        int b = 4;

        // 正号：+
        System.out.println(+a);

        // 负号：-   负负会得正
        System.out.println(-b);

        // 加：+
        System.out.println(a + b);

        // 减：-
        System.out.println(a - b);

        // 乘：*
        System.out.println(a * b);

        // 除：/
        System.out.println(b / a);

        // 取余(取模)：%
        System.out.println(b % a);

        // 自增(前)：++
        System.out.println("自增前：" + +a);

        // 自增(后)：++
        int age = 10;
        System.out.println("自增后，原来数值为：" + age++);   // 先打印10，再10+1=11
        System.out.println("自增后：" + age);               // 输出11

        // 自减(前)：--
        System.out.println("自减前：" + --a);

        // 自减(后)：--
        int num = 10;
        System.out.println("自减后，原来数值为" + num--);     // 先打印10，再10-1=9
        System.out.println("自减后：" + num);               // 输出9

        // 字符拼接：+
        char c = 'h';
        String d = "ello";
        System.out.println("字符拼接：" + c + d);

        /* 练习：求三位数长度的个个十百位数 */
        int number = 189;
        System.out.println("百位数为：" + number / 100);
        System.out.println("十位数为：" + number / 10 % 10);
        System.out.println("个位数为：" + number % 10);

        /* 自增其它数值 */
        int num1 = 10;
        num1 += 2;
        System.out.println(num1);

        /* 自增其它数值 */
        int num2 = 10;
        num2 -= 2;
        System.out.println(num2);
    }
}


