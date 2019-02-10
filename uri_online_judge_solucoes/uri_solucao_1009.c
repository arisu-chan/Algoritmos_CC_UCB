#include <stdio.h>
 
int main() {
 
  

    char nome[30];
    double sal, vendas, TOTAL;

    
    scanf("%s", nome);
    scanf("%lf", &sal);
    scanf("%lf", &vendas);

    TOTAL = sal + (vendas*15)/100;


    printf("TOTAL = R$ %.2lf\n", TOTAL);


 
    return 0;
}