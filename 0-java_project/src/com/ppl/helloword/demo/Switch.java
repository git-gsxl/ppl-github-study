package com.ppl.helloword.demo;

/*
@USER PPL-泡泡龙 or 广深小龙
@date 2020-12-12 13:34
*/

public class Switch {
    public static void main(String[] args) {
/*        String num = "2";
        switch (num) {
            case "0":
                System.out.println("0000");
            case "1":
                System.out.println("1111");
            case "2":
                System.out.println("2222");
                break;
            case "3":
                System.out.println("3333");
            case "4":
                System.out.println("4444");
        }*/

        //⒉.对学生成绩大于60分的，输出“合格”。低于60分的，输出“不合格”。
        int score = 88;
        switch (score / 60) {
            case 0:
                System.out.println("不及格");
                break;
            case 1:
                System.out.println("及格");
                break;
            default:
                System.out.println("请确认您的分数范围是否为0-100？");
        }
    }
}
