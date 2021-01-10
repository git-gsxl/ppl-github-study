package com.Extends;

/*
@USER PPL-泡泡龙 or 广深小龙
@date 2021-01-03 21:41
*/

public class Person {
    String name;
    int age;
    private int number = 10;

    public void eat() {
        System.out.println("吃饭~");
    }

    public void sleep() {
        System.out.println("睡觉~");
    }

    public int getNumber() {
        return this.number;
    }
}
