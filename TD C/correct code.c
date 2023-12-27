#include <stdio.h>
#include <stdlib.h>
struct coord
{
    int x;
    int y;
};
int main()
{

    int i, n;
    FILE *pointer;                        // FILE pointer;
    pointer = fopen("example.txt", "r+"); // pointer = fopen("example.txt","w+");
    struct coord e;                       // coord e;

    if (pointer != NULL) // if(!pointer)
    {
        fscanf(pointer, "%d", &n); // fscanf(pointer, "%d", n);
        for (i = 0; i < n; i++)
        {
            fscanf(pointer, "%d", &e.x); // fscanf(pointer, "%d", e.x);
            fscanf(pointer, "%d", &e.y); // fscanf(pointer, "%d\n", e.y);

            printf("(%d, %d)\n", e.x, e.y); // printf("(%d, %d)\n", &e.x, &e.y);
        }
        fclose(pointer); // fclose(&pointer);
    }
    else
    {
        printf("Error!");
        exit(0);
    }
    return 0;
}
