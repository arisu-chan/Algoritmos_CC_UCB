#include <stdio.h>
 
int main() {
 
	
	float A, B;
	double MEDIA;
	
	A = B = 0;
	
	scanf("%f", &A);
	scanf("%f", &B);
	
	
	MEDIA = ((A*3.5)+(B*7.5))/ 11;
    
    
    printf("MEDIA = %.5lf\n", MEDIA);
 
    return 0;
}
