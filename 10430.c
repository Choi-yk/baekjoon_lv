#include <stdio.h>

int main()
{
    int A, B, C;
    
    scanf_s("%d %d %d", &A, &B, &C);
    
    printf("%d\n", (A+B)%C);
    printf("%d\n", ((A%C)+(B%C))%C);
    printf("%d\n", (A*B)%C);
    printf("%d\n", ((A%C)*(B%C))%C);

}
