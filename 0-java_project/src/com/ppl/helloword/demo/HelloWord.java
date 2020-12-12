package com.ppl.helloword.demo;

public class HelloWord {

    int puppyAge;

    public HelloWord(double num) {
        System.out.println(num);
    }

    //    这是一个hello word
    public void setAge(int age) {
        puppyAge = age;
        System.out.println(puppyAge);
    }

    public static void main(String[] args) {
        HelloWord my_helloWord = new HelloWord(1564.55555);
        my_helloWord.setAge(5);

    }
}
