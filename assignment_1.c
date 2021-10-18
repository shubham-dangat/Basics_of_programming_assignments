#include<stdio.h>
#include <math.h>

int main()
{
float r1=12,r2=10;
float theta1=90,theta2=45;
float r,theta,y;

theta=(theta1+theta2)/2;                       //formula to find 'r' of point D.

y=(theta1-theta2)/2;

r=2*r1*r2*cos((y*(22/7))/180)/(r1+r2);        //formula to find 'theta' of point D.

printf("To find coordinates of point 'D' which intersects line joining 'A' and 'B' and angle bisector of angle AOD ");
printf("\nA(r1,\u03B81)=(%f,%f)",r1,theta1);
printf("\nO(r',\u03B8')=(0,0)");
printf("\nB(r2,\u03B82)=(%f,%f)",r2,theta2);
printf("\nD(r,\u03B8)=(%f,%f)",r,theta);
}

/*
Output:

To find coordinates of point 'D' which intersects line joining 'A' and 'B' and angle bisector of angle AOD 
A(r1,θ1)=(12.000000,90.000000)
O(r',θ')=(0,0)
B(r2,θ2)=(10.000000,45.000000)
D(r,θ)=(10.150992,67.500000)

*/