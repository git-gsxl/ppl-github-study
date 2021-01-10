package com.Extends;

/*
@USER PPL-泡泡龙 or 广深小龙
@date 2021-01-03 21:44
*/

public class ExtendsTest {
    public static void main(String[] args) {
        Student s = new Student();
        s.age = 18;
        s.name = "PPL";
        s.eat();
        s.sleep();
        s.study();
        System.out.println(s.getNumber());
    }
}
