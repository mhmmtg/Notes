package com.mguler.Chapter01;

public class Errors {
    //Syntax Error
    public static void main(String[] args) { //-void
        System.out.println("Welcome to Java"); //-2nd (")

        //Runtime Error
        System.out.println(1 / 0);

        //Logic Error
        System.out.println("Celsius 35 is Fahrenheit degree ");
        System.out.println((9 / 5) * 35 + 32);
    }
}
