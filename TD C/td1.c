// TD1 by Matthieu TOURRETTE TC02 in NF05A - UTT

// Exercice 1:
#include <stdio.h>

void today_date()
{
    int nb_day, nb_month, nb_year, nb_week;

    printf("Enter the number of this day: ");
    scanf("%d", &nb_day);

    printf("Enter the number of this month: ");
    scanf("%d", &nb_month);

    printf("Enter the number of this year: ");
    scanf("%d", &nb_year);

    printf("Enter the number of this week: ");
    scanf("%d", &nb_week);

    printf("Today, we are the %d/%d/%d, and we are the week number %d!", nb_day, nb_month, nb_year, nb_week);
}

void ask_email()
{
    char email[100];

    printf("\nEnter your email adress here: ");
    scanf("%s", email);

    printf("Your email adress is: %s", email);
}

int main()
{
    printf("Hello world!\n");
    today_date();
    ask_email();
    return 0;
}

// Exercice 2:

#include <stdio.h>

int main()
{
    int i = 0; // division by 0, it's impossible for the computer, so it goes to an error. We have to change the value of i to correct the program.
    int j = 5;

    printf("Division de j par i = %d", j / i);
    return 0;
}

// Exercice 3:

#include <stdio.h>

int main()
{
    printf("Size of int: %d", sizeof(int));
    printf("\nSize of short: %d", sizeof(short));
    printf("\nSize of char: %d", sizeof(char));
    printf("\nSize of float: %d", sizeof(float));
    printf("\nSize of double: %d", sizeof(double));
    return 0;
}

// Exercice 4:

#include <stdio.h>

void run_one()
{
    int a, b;
    int sum, diff, product, quotient, reminder;

    printf("Enter the value (non zero) of a: ");
    scanf("%d", &a);

    printf("Enter the value (non zero) of b: ");
    scanf("%d", &b);

    sum = a + b;
    diff = a - b;
    product = a * b;
    quotient = a / b;
    reminder = a % b;

    printf("The sum is: %d, the difference is: %d, the product is: %d, the quotient is: %d, and the reminder of the division is: %d.", sum, diff, product, quotient, reminder);
}

void run_two_f()
{
    float a, b, c;

    printf("Enter the value of a: ");
    scanf("%f", &a);

    printf("Enter the value of b: ");
    scanf("%f", &b);

    printf("Before swapp: a = %f and b = %f", a, b);
    c = a;
    a = b;
    b = c;
    printf("\nAfter swapp: a = %f and b = %f", a, b);
}

void run_two_c()
{
    char a[2], b[2], c[2];

    printf("Enter the value of a: ");
    scanf("%s", a);

    printf("Enter the value of b: ");
    scanf("%s", b);

    printf("Before swapp: a = %s and b = %s", a, b);
    c[0] = a[0];
    a[0] = b[0];
    b[0] = c[0];
    printf("\nAfter swapp: a = %s and b = %s", a, b);
}

void run_three()
{
    char a[2], b[2], sum, diff;

    printf("Enter the value of a: ");
    scanf("%s", a);

    printf("Enter the value of b: ");
    scanf("%s", b);

    sum = a[0] + b[0];
    diff = a[0] - b[0];
    printf("The sum is: %c, and the difference is: %c.", sum, diff);
}

void run_four()
{
    float a, b;
    float max, min;

    printf("Enter the value of a: ");
    scanf("%f", &a);

    printf("Enter the value of b: ");
    scanf("%f", &b);

    if (a >= b)
    {
        max = a;
        min = b;
    }
    else
    {
        max = b;
        min = a;
    }

    printf("The value of the maximum is: %f, and the minimum is: %f.", max, min);
}

int main()
{
    run_one();
    run_two_f();
    run_two_c();
    run_three();
    run_four();
    return 0;
}

// Exercice 5: To complete

A += (unsigned short)C; // change the type of C
A = ~A;                 //
B = A ^ (A + 2);        // B is equal to A power A+2
C = (...)(A << B);      //
A = A & (...)C;         //

// unsigned short is the same type as int, but in positive, signs can change between two of them.

// Exercice 6: To complete

#include <stdio.h>

int main()
{
    int x, n, p;

    printf("Enter x: ");
    scanf("%d", &x);

    printf("Enter n: ");
    scanf("%d", &n);

    printf("Enter p: ");
    scanf("%d", &p);

    return 0;
}

// Exercice 7:

#include <stdio.h>

int main()
{
    int B, H;
    // printf("%d ; %d", B, H); B and H have random values attributed by the computer, if there is no affectation.
    int A;

    B = 7;
    H = 9;
    A = 0.5 * B * H;

    printf("The area of the triangle base is: %d", A);

    return 0;
}

// Exercice 8:

#include <stdio.h>

int main()
{
    int R, H;
    float B, V;
#define PI 3.1416
    printf("%.4f", PI);

    R = 5;
    H = 10;
    B = PI * (R * R);
    V = (1.0 / 3.0) * B * H;

    printf("\nThe volume of the cone is: %.2f", V);

    return 0;
}

// Exercice 9:

#include <stdio.h>
#include <math.h>

void convert_deci_bin()
{
    int nb, nb_bin, start, bin, a;

    printf("Enter the number who want to convert to binary: ");
    scanf("%d", &nb);
    start = nb;
    a = 1;
    nb_bin = 0;

    while (start != 0)
    {
        bin = start % 2;
        start = start / 2;
        nb_bin = nb_bin + (a * bin);
        a = a * 10;
    }

    printf("The number %d in binary is: %d", nb, nb_bin);
}

void convert_bin_deci()
{
    int nb, nb_bin, start, dec, a;

    printf("\nEnter the binary number who want to convert to decimal: ");
    scanf("%d", &nb_bin);
    start = nb_bin;
    a = 0;
    nb = 0;

    while (start != 0)
    {
        dec = start % 10;
        start = start / 10;
        nb = nb + dec * pow(2, a);
        a++;
    }

    printf("The binary number %d in decimal is: %d", nb_bin, nb);
}

int main()
{
    convert_deci_bin();
    convert_bin_deci();
    return 0;
}
