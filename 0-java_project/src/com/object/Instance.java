package com.object;

/*
@USER PPL-泡泡龙 or 广深小龙
@date 2020-12-20 17:47
*/

public class Instance {
    public static void main(String[] args) {

        // 正常实例化
        PersonT p = new PersonT();
        p.GetAge();

        // 匿名实例化
        new PersonT().GetAge();
    }
}

class PersonT {
    int age = 8;

    public void GetAge() {
        System.out.println(age);
    }
}
