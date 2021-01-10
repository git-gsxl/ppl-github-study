package com.object1223;

/*
@USER PPL-泡泡龙 or 广深小龙
@date 2020-12-27 14:22
*/

public class PersonTest {
    public static void main(String[] args) {

        // 创建类的对象，默认是空参数
//        Person p = new Person();

        // 在new的时候传入参数，初始化属性
        Person p = new Person("PPL");
        System.out.println(p.GetName());
    }
}

class Person {
    String name;
    // 存在多个重名的构造器，那么就是构造器的重载
    // 构造器1
    public Person(String str) {
        name = str;
    }

    // 构造器2
    public Person() {
        System.out.println("构造器2");
    }

    //方法
    public String GetName() {
        return name;
    }
}