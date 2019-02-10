#include <stdio.h>
 
int main() {
 
    int hrs, h;
    float amount, dollar;
    scanf("%d %d %f",&hrs, &h, &amount);
    dollar = h * amount;
    printf("NUMBER = %d\n",hrs);
    printf("SALARY = U$ %.2f\n",dollar);
 
    return 0;
}