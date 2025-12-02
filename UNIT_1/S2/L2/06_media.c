#include <stdio.h>

int main() {
    int x;
    int y;
    float media;

    printf("Inserisci il primo numero: ");
    scanf("%d" , &x);

    printf("Inserisci il secondo numero: ");
    scanf("%d" , &y);

    media = (x + y)/2;

    printf("La media è: %f" , media);

    return 0;
}