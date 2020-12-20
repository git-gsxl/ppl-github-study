package com.object;

/*
@USER PPL-泡泡龙 or 广深小龙
@date 2020-12-20 12:42
*/

public class Person {
    public static void main(String[] args) {
        PersonTest p1 = new PersonTest();
        p1.name = "ppl";
        p1.age = 18;
        p1.isMale = true;
        p1.eat();
        p1.sleep();
        p1.talk();
    }

}

class PersonTest {

    // 属性
    String name;
    int age;
    boolean isMale;

    // 方法
    public void eat() {
        System.out.println("人吃什么？答：人间烟火");
    }

    public void sleep() {
        System.out.println("人需要睡觉休息，专家建议每天睡眠至少8小时");
    }

    public void talk() {
        System.out.println("人可以说话，但我说的是中文");
    }
}
