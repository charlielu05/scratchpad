#include <stdio.h>
#include <stdlib.h>
int main(int argc, char **argv) {
   for (int i = 1; i < argc; i++) {
      // read file
      FILE *fp = fopen(argv[i], "r");

      if (fp == NULL) {
         printf("wcat: cannot open file\n");
         exit(1);
      }
      else {
         printf("\n%s file read success\n", argv[i]);
      }

      // print out contents
      char text_buffer[256];
      while (fgets(text_buffer, sizeof(text_buffer), fp) != NULL) {
         printf("%s", text_buffer);
      }

      fclose(fp);
   }
   printf("\n");
   return 0;
}
