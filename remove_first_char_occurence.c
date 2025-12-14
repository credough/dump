#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char firstocc_remover(int i, char word[], int length, char will_remove);
int main()
{
    printf("word buyoyer haha jk tatangalin lang first occurence\n");

    char word [100];
    printf("\n");
    printf("pls enter the word: \n");
    scanf("%s", word);
    printf("\n");
    int length = strlen(word);
    char will_remove;
    printf("character to remove:\n");
    scanf(" %c", &will_remove);
    int i = 0;

    char new_word = firstocc_remover(i, word, length, will_remove);


    printf("New word with removed %c: %s\n", new_word, word);
    return 0;
}

char firstocc_remover(int i, char word[], int length, char will_remove){

    while (i < length){
        if (word[i] == will_remove){
                break;
        } else {
            i++;
        }
    }

    while(i < length){
        word[i] = word[i + 1];
        i++;
    }
    return word[i];
}
