#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char **argv) {
    if (argc < 2) {
        printf("wgrep: searchterm [file ...]\n");
        exit(1);
    }
    // search term
    char *term = argv[1];
    
    printf("search term: %s\n", term);

    // loop through file
    for (int i=2; i< argc; i++) {
        // file pointer
        FILE *fp = fopen(argv[i], "r");

        char text_buffer[256];

        // go through files
        while (fgets(text_buffer, sizeof(text_buffer), fp) != NULL) {
            if (strstr(text_buffer, term) != NULL) {
                printf("%s", text_buffer);
            }
        }

    }

    return(0);
}
