#include <stdio.h>

int main() {
    long unsigned int n0,n;
    long unsigned register int  sum_numbers;
    scanf("%lu",&n0);
    scanf("%lu",&n);
if(1 <= n0 && (n <= 100000000000) && (n0 & 1) || ~(n & 1)){
    sum_numbers = ((n - n0 + 1)*(n+n0))/2;
    printf("%lu",sum_numbers);
}
	return 0;
}
