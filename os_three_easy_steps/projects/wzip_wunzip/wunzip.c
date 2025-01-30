#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char **argv) {
    // source file
    char *source = argv[1];
    FILE *source_file = fopen(source, "r");

    int count;
    char current_char;

    while (fread(&count, sizeof(int), 1, source_file) == 1) {
        fread(&current_char, sizeof(char), 1, source_file);
        for (int i = 0; i < count; i++) {
            printf("%c", current_char);
        }
    }

    fclose(source_file);

    return(0);
}


