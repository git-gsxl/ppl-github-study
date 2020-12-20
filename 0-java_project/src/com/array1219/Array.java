package com.array1219;

/*
@USER PPL-泡泡龙 or 广深小龙
@date 2020-12-19 14:04
*/

public class Array {
    public static void main(String[] args) {
        // 静态初始化
        int[] numbers = new int[]{1, 2, 3, 4, 5};

        // 动态初始化
        String[] names = new String[5];
        names[0] = "泡泡龙";
        names[1] = "广深小龙";
        names[2] = "龙小龙";
        names[3] = "PPL";
        names[4] = "小龙";

        // 获取数组长度
        System.out.println("长度为：" + names.length);

        // 索引获取数组的值
        System.out.println(names[0]);

        // 遍历数组
        for (int i = 0; i < names.length; i++) {
            System.out.println(names[i]);
        }
    }

}
