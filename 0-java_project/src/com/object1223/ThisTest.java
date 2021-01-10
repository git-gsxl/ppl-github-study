package com.object1223;

/*
@USER PPL-泡泡龙 or 广深小龙
@date 2020-12-27 15:32
*/

public class ThisTest {
    public static void main(String[] args) {
        Person1 p1 = new Person1();
        p1.setName("PPL");
        System.out.println(p1.getName());
    }
}

class Person1 {
    String name;

    public void setName(String name) {
        name = name;        // 方法的形参与类的属性重名的情况下，又想重名咋办？
        this.name = name;   // 可以使用this关键字，声明为类的属性；
    }

    public String getName() {
        return name;
    }
}