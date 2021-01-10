package com.interview;

/*
@USER PPL-泡泡龙 or 广深小龙
@date 2020-12-21 22:00
*/

public class Interview3 {
    public static void main(String[] args) {

        int[] arr = new int[10];
        System.out.println(arr);        // 输出地址值

        char[] arr1 = new char[2];
        System.out.println(arr1);       // 为啥是空？

        char[] arr2 = {'a', 'b'};
        System.out.println(arr2);       // 输出的是 a b
    }
}
