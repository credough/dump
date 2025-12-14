#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void print_reverse(char string[], int length){
    for(int i = length; i >= 0; i--){
        printf("%c", string[i]);
    }
    printf("\n");

}
int main()
{
    char choice;

    do {
    char mystring[100];
    printf("Input a word to reverse:\n");
    scanf("%s", mystring);
    int length = strlen(mystring) - 1;

    print_reverse(mystring, length);

    printf("Continue? (y - yes / n - no)\n");
    scanf(" %c", &choice);
    printf("\n");

    }while (choice == 'y' || choice == 'Y');

}
