package com.object1220;

/*
@USER PPL-泡泡龙 or 广深小龙
@date 2020-12-20 20:18
*/

public class Args {

    // 可变个数形参
    public void eat(String... food) {
        // 遍历可变形参
        String strs = "";
        for (int i = 0; i < food.length; i++) {
            strs += food[i] + " ";
        }
        System.out.println(strs);
    }

    public void eat(String food) {
        System.out.println("重载：" + food);
    }

    public void eat(int count) {
        System.out.println("重载，每天吃几次？：" + count);
    }

    public static void main(String[] args) {
        Args a = new Args();
        a.eat("1", "2", "3", "PPL");
        a.eat("米饭");
        a.eat(3);
    }
}
