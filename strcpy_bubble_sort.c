#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

// dito chinecheck kung walang number
int checkname(char pangalan[]) {
    for (int i = 0; i < strlen(pangalan); i++) {
        if (isdigit(pangalan[i])) {
            return 1; // may number (bawal)
        }
    }
    return 0; // return zero kapag valid (walang name)
}


// function o formula na magaarrange alphabetically
//bubble sort yan tol search mo na lang (swapping if false/true)
void sortNames(char names[5][100]) {
    char temp[100];

    for (int i = 0; i < 4; i++) {
        for (int j = i + 1; j < 5; j++) {
            if (strcmp(names[i], names[j]) > 0) {
                // Swap names[i] and names[j]
                strcpy(temp, names[i]);
                strcpy(names[i], names[j]);
                strcpy(names[j], temp);
            }
        }
    }
}

int main() {
    char pangalan[5][100];

    printf("Pakilagay ng limang pangalan:\n");
    for (int i = 0; i < 5; i++) {
        while (1) {
            printf("Pangalan %d: ", i + 1);
            scanf("%s", pangalan[i]);

            if (checkname(pangalan[i])) { //kapag return 1 yung function kanina means true
                printf("Bawal may number tol. Ulett\n");
            } else {
                break;
            }
        }
    }

    // tinatawag mo na yung function
    sortNames(pangalan);

    // Output
    printf("\nmga pangalan na nakaarrange (a-z):\n");
    for (int i = 0; i < 5; i++) {
        printf("%s\n", pangalan[i]);
    }

    return 0;
}

