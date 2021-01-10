package com.object1223;

/*
@USER PPL-泡泡龙 or 广深小龙
@date 2020-12-27 15:54
*/

public class ThisC {
    public static void main(String[] args) {
        ThisCTest t = new ThisCTest("PPL", 18);
        System.out.println(t.getAge());
        System.out.println(t.getName());
    }
}

class ThisCTest {
    private String name;
    private int age;

    // 构造器1
    public ThisCTest() {
        System.out.println("创建对象初始化：正在初始化中...");
    }

    // 构造器2
    public ThisCTest(String name) {
        this();         // this(形参)，既调用：构造器1
        this.name = name;
    }

    // 构造器3
    public ThisCTest(String name, int age) {
        this(name);     // this(形参)，既调用：构造器2
        this.age = age;
    }

    public int getAge() {
        return age;
    }

    public String getName() {
        return name;
    }
}