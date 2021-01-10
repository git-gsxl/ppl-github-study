package com.interview;

/*
@USER PPL-泡泡龙 or 广深小龙
@date 2020-12-21 21:36
*/

import java.util.Arrays;

public class Interview1 {
    public static void main(String[] args) {

        /*
         * 定义一个int型的数组:{10, 3, 234, 234, 12, 123, 34, 86};
         * 让数组的每个位置上的值去除以首位置的元素，得到的结果，作为该位置上的新值。遍历新的数组。
         */

        int[] arr = {10, 3, 234, 234, 12, 123, 34, 86};
//         for (int i = 0; i < arr.length; i++) {       // 错误写法

        // 方法一：倒着来可以的
        for (int i = arr.length - 1; i >= 0; i--) {
            arr[i] = arr[i] / arr[0];
        }
        System.out.println(Arrays.toString(arr));

        // 方法二：用变量来先赋值下标为0的数值
        int[] arr2 = {10, 3, 234, 234, 12, 123, 34, 86};
        int temp = arr2[0];
        for (int i = 0; i < arr.length; i++) {
            arr2[i] = arr2[i] / temp;
        }
        System.out.println(Arrays.toString(arr2));
    }
}
