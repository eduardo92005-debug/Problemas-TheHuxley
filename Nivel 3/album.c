#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main ( )
{
    int x, y , l1 , h1, l2, h2;

    scanf("%d %d",&x,&y);
    scanf("%d %d",&l1,&h1);
    scanf("%d %d",&l2,&h2);
    if (((l1+l2 <= x) && (h1<=y && h2<=y )) ||
        ((h1+h2 <= x) && (l1<=y && l2<=y )) ||
        ((l1+l2 <= y) && (h1<=x && h2<=x )) ||
        ((h1+h2 <= y) && (l1<=x && l2<=x )) ||
        ((l1+h2 <= x) && (h1<=y && l2<=y )) ||
        ((l1+h2 <= y) && (h1<=x && l2<=x )) ||
        ((l2+h1 <= x) && (l1<=y && h2<=y )) ||
        ((l2+h1 <= y) && (l1<=x && h2<=x ))
        ){
            printf("S");
        }else{
            printf("N");
        }
    return 0 ;
}
