package com.object;

/*
@USER PPL-泡泡龙 or 广深小龙
@date 2020-12-20 12:15
*/

public class ObjectTest {
    public static void main(String[] args) {
        User user = new User();
        user.name = "泡泡龙";
        user.age = 18;
        user.eat("米饭");
    }
}

class User {

    // 类的变量
    String name;
    int age;

    public void eat(String food) {
        System.out.println("姓名：" + name + " 吃的是什么？ 答案：" + food);
        System.out.println("年龄只有：" + age);

        String IsMale = "true";  // 方法的变量（局部变量）
        System.out.println("我是局部变量：" + IsMale);
    }
}