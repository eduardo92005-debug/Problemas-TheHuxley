#include <stdio.h>

int encaixa(int a, int b)
{
const int BASE = 10;
register int digitos=0,i=0,aux=b,powered = 10;
if(0 <= a || 0 <= b && b <= 9999999){
    while(aux != 0){
          digitos++;
          aux = aux/10;
    }
    while(i < digitos-1){
         powered *= BASE;
         i++;
    }
    if(a % powered == b){
         return 1;
    } else {
         return 0;
    }
}
}

int main(void) 
{
    int x, y;
    
    scanf("%d%d", &x, &y);
    while (x != -1) // l� enquanto x for diferente de -1
    {
        printf("%d\n", encaixa(x, y) );
        scanf("%d%d", &x, &y);
    }
	return 0;
}

