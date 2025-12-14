#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

int main()
{   //               01234567
    char salita[] = "AGING";
    int length = strlen(salita);

    srand(time(NULL));

    int random_num = rand() % length;
    int temp;

    for (int i = 0; i < length; i++){
        temp = salita[i];
        salita[i] = salita[random_num];
        salita [random_num] = temp;
    }
char answer[length];
    printf("Guess a scramble word below:\n");
    printf("%s", salita);
    printf("\n");
    printf("your answer:\n");
    scanf("%s", &answer);

    char orig[] = "AGING";

    if(strcmp(orig, answer) == 0){
        printf("Congrats you are correct!");
    } else {
        printf("You are wrong! The correct answer is %s\n", orig);
    }


    return 0;
}
