#include <stdio.h>
 
int main() {
 
    int codPeca1 = 0, numPecas1 = 0, codPeca2 = 0, numPecas2 = 0;
    float valorPeca1 = 0, valorPeca2 = 0;

    scanf("%d %d %f", &codPeca1, &numPecas1, &valorPeca1);
    scanf("%d %d %f", &codPeca2, &numPecas2, &valorPeca2);

    printf("VALOR A PAGAR: R$ %.2f\n", numPecas1*valorPeca1 + numPecas2*valorPeca2);

 
    return 0;
}
