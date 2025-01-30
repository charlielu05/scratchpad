#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char **argv) {
    // source file
    char *source = argv[1];
    FILE *soure_file = fopen(source, "r");
    
    // output file
    char *output = argv[2];
    FILE *output_file = fopen(output, "w+");

    char last_char[2];
    char current_char[2];
    // counter
    int i = 0;
    int is_initialized = 0;

    while (fgets(current_char, sizeof(current_char), soure_file) != NULL) {
        if (!is_initialized) {
            strcpy(last_char, current_char);
            is_initialized = 1; // Set the flag to true after initialization
            i = 0;
            }
        if (strcmp(current_char, last_char) == 0) {
            i++;
        }
        else {
            printf("%d %s\n", i, last_char);
            fwrite(&i, sizeof(int),1, output_file);
            fwrite(last_char, sizeof(char), 1, output_file);
            strcpy(last_char, current_char);
            i = 1;
        }
    }

    if (is_initialized) {
        printf("%d %s\n", i, last_char);
        fwrite(&i, sizeof(int),1, output_file);
        fwrite(last_char, sizeof(char), 1, output_file);
    }

    fclose(soure_file);
    fclose(output_file);

    return(0);
}
