package com.object;

/*
@USER PPL-泡泡龙 or 广深小龙
@date 2020-12-20 16:20
*/

public class ClassM {
    public static void main(String[] args) {
        ClassTest m = new ClassTest();
        m.eat("米饭");
        System.out.println(m.name);
        System.out.println(m.getName());
        System.out.println(m.returnName());

        // 引用类型
        ClassTest[] st = new ClassTest[3];
        st[0] = new ClassTest();
        System.out.println("111" + st[0].name);
    }
}

class ClassTest {

    // 类属性
    String name = "泡泡龙";

    // 形参：food，可以多个逗号分开
    public void eat(String food) {
        System.out.println("吃的是：" + food);
    }

    // 有返回值：return，需指定返回的类型，比如：String
    // 但是命名指定了返回值的类型，就一定要有：return返回值
    public String getName() {
        eat("面条");      // 方法内部调用方法
        return name;
    }

    // 判断语句，需要在各个分支都要return
    public String returnName() {
        if ("泡泡".contains(name)) {
            return name;
        } else if ("泡泡龙".contains(name)) {
            return "1";
        } else {
            return "-1";
        }
    }
}
