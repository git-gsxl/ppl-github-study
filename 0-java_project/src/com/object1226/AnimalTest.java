package com.object1226;

/*
@USER PPL-泡泡龙 or 广深小龙
@date 2020-12-26 22:42
*/

public class AnimalTest {
    public static void main(String[] args) {
        Animal ani = new Animal();
        ani.setAge(10);
//        System.out.println(ani.age);

        // 私有的，查，独立封装一个get方法
        System.out.println(ani.getAge());
    }
}

class Animal {
    private int age;

    public void setAge(int updateAge) {
        if (updateAge >= 0 && updateAge % 2 == 0) {
            age = updateAge;
        } else {
            age = 0;
            System.out.println("年龄输入必须为正数！");
        }
    }

    public int getAge() {
        if (age >= 0 && age % 2 == 0) {
            return age;
        } else {
            age = 0;
            System.out.println("已默认为：0");
            return age;
        }
    }
}