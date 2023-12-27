// TD5 by Matthieu TOURRETTE TC02 in NF05A - UTT
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>
#define MAX 25

// EXERCICE 1:
int insert_vector(int N, FILE *fp)
{
    int i;
    float *vector;
    vector = calloc(N, sizeof(float));
    for (i = 0; i < N; i++)
    {
        printf("Enter the value of the %dth element: ", i + 1);
        scanf("%f", (vector + i));
    }
    // fprintf(fp,"Print of the vector:\n");
    for (int i = 0; i < N; i++)
    {
        // fprintf(fp,"The value of the %dth element is: %.2f\n", i+1, *(vector+i));
        fprintf(fp, "%.2f\t", *(vector + i));
    }
    fprintf(fp, "\n");
    return 0;
}

int sum_vector(int N, FILE *fp)
{
    rewind(fp);
    int i;
    float *vectsum;
    float *vect1;
    float *vect2;
    vectsum = calloc(N, sizeof(float));
    vect1 = calloc(N, sizeof(float));
    vect2 = calloc(N, sizeof(float));
    for (i = 0; i < N; i++)
    {
        fscanf(fp, "%f", (vect1 + i));
    }
    for (i = 0; i < N; i++)
    {
        fscanf(fp, "%f", (vect2 + i));
    }
    fseek(fp, 0, SEEK_END);
    for (i = 0; i < N; i++)
    {
        vectsum[i] = vect1[i] + vect2[i];
    }
    fprintf(fp, "\nPrint of the sum of the vectors:\n");
    for (i = 0; i < N; i++)
    {
        fprintf(fp, "The value of the %dth element is: %.2f\n", i + 1, *(vectsum + i));
    }
    fprintf(fp, "\n");
    return 0;
}

int main()
{
    FILE *fp;
    char name[25], txt[5] = ".txt";
    printf("How do you want to name the file? ");
    scanf("%s", name);
    strcat(name, txt);
    fp = fopen(name, "w+");
    int M, N;
    printf("How many vectors do you want? ");
    scanf("%d", &M);
    printf("What's the size of your vectors? ");
    scanf("%d", &N);
    for (int i = 0; i < M; i++)
    {
        insert_vector(N, fp);
    }
    sum_vector(N, fp);
    fclose(fp);
    return 0;
}

typedef enum
{
    Loaned,
    Available
} bookState;
typedef struct
{
    int day;
    int month;
    int year;
} date;
typedef struct
{
    char author[20];
    char title[100];
    char rib[9];
    int year;
    char editor[20];
    bookState state;
    date loanDate;
} LibBook;

LibBook enter_info(LibBook book)
{
    char trash[1];
    scanf("%c", &trash[0]);

    printf("Enter the title of the book: ");
    gets(book.title);
    printf("Enter the RIB of the book: ");
    gets(book.rib);
    printf("Enter the name of the author: ");
    gets(book.author);
    printf("Enter the editor of the book: ");
    gets(book.editor);
    printf("Enter the year of publication: ");
    scanf("%d", &book.year);
    printf("Enter the availability of the book: (0 for loanned and 1 for available) ");
    scanf("%d", &book.state);
    if (book.state == Loaned)
    {
        printf("Enter the day of loan: ");
        scanf("%d", &book.loanDate.day);
        printf("Enter the month of loan: ");
        scanf("%d", &book.loanDate.month);
        printf("Enter the year of loan: ");
        scanf("%d", &book.loanDate.year);
    }
    return book;
}

int write_in_file(FILE *fp, int N)
{
    LibBook book;
    fprintf(fp, "Number of books: %d\n\n", N);
    for (int i = 0; i < N; i++)
    {
        book = enter_info(book);
        write_file(fp, book);
    }
    return 0;
}

void write_file(FILE *fp, LibBook book)
{
    fprintf(fp, "title of the book:\t%s\n", book.title);
    fprintf(fp, "RIB of the book:\t%s\n", book.rib);
    fprintf(fp, "name of the author:\t%s\n", book.author);
    fprintf(fp, "editor of the book:\t%s\n", book.editor);
    fprintf(fp, "year of the publication:\t%d\n", book.year);
    fprintf(fp, "availability of the book: (0 for loanned and 1 for available)\t%d\n", book.state);
    if (book.state == Loaned)
    {
        fprintf(fp, "day of loan:\t%d\n", book.loanDate.day);
        fprintf(fp, "month of loan:\t%d\n", book.loanDate.month);
        fprintf(fp, "year of loan:\t%d\n", book.loanDate.year);
    }
    fputs("\n", fp);
}

int read_file(FILE *fp)
{
    int N, i = 0;
    LibBook *books;
    rewind(fp);
    char buffer[MAX];
    char c;
    fscanf(fp, "%*s %*s %*s %d", &N);
    books = calloc(N, sizeof(LibBook));

    fseek(fp, 2, SEEK_CUR);

    while ((c = fgetc(fp)) != EOF)
    {
        if (c == '\t')
        {
            fgets(buffer, MAX, fp);
            *(books + i)->author = buffer;
        }
    }
    printf("%s", *(books + i)->title);

    return 0;
}

int main()
{
    LibBook book1;
    int N;
    FILE *fp;
    char name[25], txt[5] = ".txt";
    printf("How do you want to name the file? ");
    scanf("%s", name);
    strcat(name, txt);
    fp = fopen(name, "r");
    book1 = enter_info(book1);
    printf("How many books have you? ");
    scanf("%d", &N);
    write_in_file(fp, N);
    read_file(fp);
    fclose(fp);
    return 0;
}
