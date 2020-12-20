package com.array1219;

/*
@USER PPL-泡泡龙 or 广深小龙
@date 2020-12-19 23:34
*/

public class ArrayMany {
    public static void main(String[] args) {
        // 静态初始化
        int[][] number = new int[][]{{1, 2, 3}, {3, 4}, {4, 5, 6, 7, 8}};
        int[][] num = {{1, 2, 3}, {}};

        System.out.println(number[0][2]);   // number下标0，则为第一组数据，[2]下标2的值
        System.out.println(number[0].length);
        System.out.println(number.length);

        String[][] str = {{"1", "泡泡龙"}, {"2", "广深小龙"}};
        System.out.println(str[0]); // 指向0数组的内存地址

        // 遍历二维数组(多维数组就用多次循环)
        for (int i = 0; i < str.length; i++) {
            for (int j = 0; j < str[i].length; j++) {
                System.out.print(str[i][j] + " ");
            }
            System.out.println();
        }
    }
}
