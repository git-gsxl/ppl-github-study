package com.ppl.helloword.demo;

/*
@USER PPL-泡泡龙or广深小龙
@date 2020-12-13 15:15
*/

public class Array {
    public static void main(String args[]) {
        int[] number = {1, 3, 5, 7, 9};
        int max = number[0];
        for (int i = 0; i < number.length; i++) {
            System.out.println(number[i]);
            if (number[i] > max) {
                max = number[i];
            }
        }
        System.out.println(number.length);
        System.out.println("最大值为：" + max);

        String[] str = {"泡泡龙", "广深小龙", "PPL"};
        for (String newStr : str) {
            System.out.println(newStr);
        }
        String[][] MyList = new String[1][2];
    }
}