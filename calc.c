#include<stdio.h>

double calculate(double  a,double b,char  op)
{
    switch(op)
    {
        case '+':
        return a+b;
        case '-':
        return a-b;
        case '*':
        return a*b;
        case '/':
        return (b!=0) ? a/b :0;
        default :
        return 0; //unknown operator 

    }
}