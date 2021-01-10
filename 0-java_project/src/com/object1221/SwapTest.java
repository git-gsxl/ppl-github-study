package com.object1221;

/*
@USER PPL-泡泡龙 or 广深小龙
@date 2020-12-21 21:10
*/

public class SwapTest {

    /*
    * 值传递机制：
    *   1、基本类型，则为真实存在的数据值；
    *   2、引用类型，此为存储数据的地址值；
    * */

    /*交换值方法，形参为：引用类型(既对象)*/
    public void swap(Data data) {
        int temp = data.n;
        int n = data.m;
        data.m = temp;
    }

    public static void main(String[] args) {
        Data data = new Data();
        data.m = 10;
        data.n = 20;
        SwapTest resSwap = new SwapTest();
        resSwap.swap(data);
        System.out.println(data.m);
        System.out.println(data.n);
    }
}

/*Data类*/
class Data {
    int m;
    int n;
}