package com.array1219;

/*
@USER PPL-泡泡龙 or 广深小龙
@date 2020-12-20 10:46
*/

import java.util.Arrays;

public class ArrayTest {
    public static void main(String[] args) {
        int[] arrInt1 = {1, 2, 3, 4, 5};
        int[] arrInt2 = {6, 2, 3, 4, 5};

        // 判断两个数组，是否相等：equals
        boolean isEq = Arrays.equals(arrInt1, arrInt2);
        System.out.println(isEq);

        // 数组输出为字符串
        System.out.println(Arrays.toString(arrInt1));

        // 排序，从小到大
        Arrays.sort(arrInt2);
        System.out.println(Arrays.toString(arrInt2));

        // 将值放入数组中
        Arrays.fill(arrInt1, 1);
        System.out.println(Arrays.toString(arrInt1));

        // 二分查找（前提是数组值小到大排序，可先使用sort）
        int[] number = {45, 4, 5, 6, 8, 55, 62, 66};
        Arrays.sort(number);    // 先排序

        int index = Arrays.binarySearch(number, 8);
        if (index >= 0) {
            System.out.println("找到下标为：" + index + " 值为：" + number[index]);
        } else {
            System.out.println("数组中不存在此数据");
        }

        // 空指针：null
        int[][] new_list = new int[2][];
        System.out.println(new_list[0][1]);
    }
}
