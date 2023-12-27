// TD3 by Matthieu TOURRETTE TC02 in NF05A - UTT
#include <stdio.h>
#include <math.h>
#include <string.h>

// Exercice 1:
void exercice1()
{
    int nb, i, val1, val2, val3;
    int tab[100];
    printf("How many integers do you want to add to th array (inferior to 100)? ");
    scanf("%d", &nb);
    for (i = 0; i < nb; i++)
    {
        printf("Write the integer number: ");
        scanf("%d", &tab[i]);
    }
    for (i = 0; i < nb; i++)
    {
        printf("%d, index %d\n", tab[i], i);
    }
    printf("What is the index of the first value? ");
    scanf("%d", &val1);
    printf("What is the index of the second value? ");
    scanf("%d", &val2);
    val3 = tab[val2];
    tab[val2] = tab[val1];
    tab[val1] = val3;
    for (i = 0; i < nb; i++)
    {
        printf("%d, index %d\n", tab[i], i);
    }
}
// Exercice 2: use fgets()
void exercice2()
{
    char car;
    int nb_low = 0, nb_up = 0, nb_space = 0;
    printf("Write a text: ");
    do
    {
        scanf("%c", &car);
        if (car > 64 && car < 91)
        {
            nb_up++;
        }
        else if (car > 96 && car < 123)
        {
            nb_low++;
        }
        else if (car == 32)
        {
            nb_space++;
        }
    } while (car != 10);
    printf("Number of upper case letters: %d, number of lower case letters: %d, number of spaces: %d", nb_up, nb_low, nb_space);
}
// Exercice 3:
void exercice3()
{
    int i, j;
    int mat1[2][2], mat2[2][2], matadd[2][2], matsous[2][2], matmul[2][2];
    mat1[0][0] = 2;
    mat1[0][1] = 4;
    mat1[1][0] = 1;
    mat1[1][1] = 0;

    mat2[0][0] = 0;
    mat2[0][1] = 1;
    mat2[1][0] = 4;
    mat2[1][1] = 2;

    // Addition
    for (i = 0; i < 2; i++)
    {
        for (j = 0; j < 2; j++)
        {
            matadd[i][j] = mat1[i][j] + mat2[i][j];
        }
    }
    // Soustraction
    for (i = 0; i < 2; i++)
    {
        for (j = 0; j < 2; j++)
        {
            matsous[i][j] = mat1[i][j] - mat2[i][j];
        }
    }
    // Multiplication
    for (j = 0; j < 2; j++)
    {
        for (i = 0; i < 2; i++)
        {
            matmul[i][j] = mat1[0][j] * mat2[i][0] + mat1[1][j] * mat2[i][1];
        }
    }

    printf("Addition of matrices: \n");
    for (i = 0; i < 2; i++)
    {
        for (j = 0; j < 2; j++)
        {
            printf("%d ", matadd[i][j]);
        }
        printf("\n");
    }
    printf("Soustraction of matrices: \n");
    for (i = 0; i < 2; i++)
    {
        for (j = 0; j < 2; j++)
        {
            printf("%d ", matsous[i][j]);
        }
        printf("\n");
    }
    printf("Multiplication of matrices: \n");
    for (i = 0; i < 2; i++)
    {
        for (j = 0; j < 2; j++)
        {
            printf("%d ", matmul[i][j]);
        }
        printf("\n");
    }
}
// Exercice 4:
#define pi 3.14159
typedef struct Complex Cplex;
struct Complex
{
    float real;
    float compl ;
};
typedef struct PolarComplex PCplx;
struct PolarComplex
{
    float module;
    float argument;
};
typedef struct Cplx Cplx;
struct Cplx
{
    float real;
    float compl ;
    float module;
    float argument;
};

void RecttoPolar()
{
    Cplex complex1;
    PCplx complex1p;
    printf("Enter the real part: ");
    scanf("%f", &complex1.real);
    printf("Enter the imaginary part: ");
    scanf("%f", &complex1.compl );
    complex1p.module = sqrt(pow(complex1.real, 2) + pow(complex1.compl, 2));
    if (complex1.real == 0)
    {
        complex1p.argument = pi;
    }
    else
    {
        float x = complex1.compl / (complex1.real + complex1p.module);
        complex1p.argument = 2 * atan(x);
    }
    printf("Argument: %f and Module: %f", complex1p.argument, complex1p.module);
}
Cplx PRecttoPolar(Cplx complex1)
{
    complex1.module = sqrt(pow(complex1.real, 2) + pow(complex1.compl, 2));
    if (complex1.real == 0)
    {
        complex1.argument = pi;
    }
    else
    {
        float x = complex1.compl / (complex1.real + complex1.module);
        complex1.argument = 2 * atan(x);
    }
    return complex1;
}

void PolartoRect()
{
    Cplex complex1;
    PCplx complex1p;
    printf("Enter the module: ");
    scanf("%f", &complex1p.module);
    printf("Enter the argument: ");
    scanf("%f", &complex1p.argument);
    complex1.real = complex1p.module * cos(complex1p.argument);
    complex1.compl = complex1p.module * sin(complex1p.argument);
    printf("Real part: %f and Imaginary part: %f", complex1.real, complex1.compl );
}
Cplx PPolartoRect(Cplx complex1)
{
    complex1.real = complex1.module * cos(complex1.argument);
    complex1.compl = complex1.module * sin(complex1.argument);
    return complex1;
}

void SumCplx()
{
    Cplx complex1, complex2, complex3, complexsum;
    int choice;
    printf("Which form of complex do you have? (0:rectangular/1:polar) ");
    scanf("%d", &choice);
    if (choice == 0)
    {
        printf("Enter the real part: ");
        scanf("%f", &complex1.real);
        printf("Enter the imaginary part: ");
        scanf("%f", &complex1.compl );
        printf("Enter the real part: ");
        scanf("%f", &complex2.real);
        printf("Enter the imaginary part: ");
        scanf("%f", &complex2.compl );
        // Sum
        complex3.real = complex1.real + complex2.real;
        complex3.compl = complex1.compl +complex2.compl ;
        complexsum = PRecttoPolar(complex3);
    }
    else if (choice == 1)
    {
        printf("Enter the module: ");
        scanf("%f", &complex1.module);
        printf("Enter the argument: ");
        scanf("%f", &complex1.argument);
        printf("Enter the module: ");
        scanf("%f", &complex2.module);
        printf("Enter the argument: ");
        scanf("%f", &complex2.argument);
        // Sum
        complex1 = PPolartoRect(complex1);
        complex2 = PPolartoRect(complex2);
        complex3.real = complex1.real + complex2.real;
        complex3.compl = complex1.compl +complex2.compl ;
        complexsum = PRecttoPolar(complex3);
    }
    else
    {
        printf("The format is not valid!");
    }
    printf("Real part: %f and Imaginary part: %f\n", complexsum.real, complexsum.compl );
    printf("Argument: %f and Module: %f\n", complexsum.argument, complexsum.module);
}

void SubCplx()
{
    Cplx complex1, complex2, complex3, complexsub;
    int choice;
    printf("Which form of complex do you have? (0:rectangular/1:polar) ");
    scanf("%d", &choice);
    if (choice == 0)
    {
        printf("Enter the real part: ");
        scanf("%f", &complex1.real);
        printf("Enter the imaginary part: ");
        scanf("%f", &complex1.compl );
        printf("Enter the real part: ");
        scanf("%f", &complex2.real);
        printf("Enter the imaginary part: ");
        scanf("%f", &complex2.compl );
        // Substraction
        complex3.real = complex1.real - complex2.real;
        complex3.compl = complex1.compl -complex2.compl ;
        complexsub = PRecttoPolar(complex3);
    }
    else if (choice == 1)
    {
        printf("Enter the module: ");
        scanf("%f", &complex1.module);
        printf("Enter the argument: ");
        scanf("%f", &complex1.argument);
        printf("Enter the module: ");
        scanf("%f", &complex2.module);
        printf("Enter the argument: ");
        scanf("%f", &complex2.argument);
        // Substraction
        complex1 = PPolartoRect(complex1);
        complex2 = PPolartoRect(complex2);
        complex3.real = complex1.real - complex2.real;
        complex3.compl = complex1.compl -complex2.compl ;
        complexsub = PRecttoPolar(complex3);
    }
    else
    {
        printf("The format is not valid!");
    }
    printf("Real part: %f and Imaginary part: %f\n", complexsub.real, complexsub.compl );
    printf("Argument: %f and Module: %f\n", complexsub.argument, complexsub.module);
}

void MulCplx()
{
    Cplx complex1, complex2, complex3, complexmul;
    int choice;
    printf("Which form of complex do you have? (0:rectangular/1:polar) ");
    scanf("%d", &choice);
    if (choice == 0)
    {
        printf("Enter the real part: ");
        scanf("%f", &complex1.real);
        printf("Enter the imaginary part: ");
        scanf("%f", &complex1.compl );
        printf("Enter the real part: ");
        scanf("%f", &complex2.real);
        printf("Enter the imaginary part: ");
        scanf("%f", &complex2.compl );
        // Multiplication
        complex3.real = complex1.real * complex2.real - complex1.compl *complex2.compl ;
        complex3.compl = complex1.real * complex2.compl +complex2.real * complex1.compl ;
        complexmul = PRecttoPolar(complex3);
    }
    else if (choice == 1)
    {
        printf("Enter the module: ");
        scanf("%f", &complex1.module);
        printf("Enter the argument: ");
        scanf("%f", &complex1.argument);
        printf("Enter the module: ");
        scanf("%f", &complex2.module);
        printf("Enter the argument: ");
        scanf("%f", &complex2.argument);
        // Multiplication
        complex1 = PPolartoRect(complex1);
        complex2 = PPolartoRect(complex2);
        complex3.real = complex1.real * complex2.real - complex1.compl *complex2.compl ;
        complex3.compl = complex1.real * complex2.compl +complex2.real * complex1.compl ;
        complexmul = PRecttoPolar(complex3);
    }
    else
    {
        printf("The format is not valid!");
    }
    printf("Real part: %f and Imaginary part: %f\n", complexmul.real, complexmul.compl );
    printf("Argument: %f and Module: %f\n", complexmul.argument, complexmul.module);
}

void DivCplx()
{
    Cplx complex1, complex2, complex3, complexdiv;
    int choice;
    float div;
    printf("Which form of complex do you have? (0:rectangular/1:polar) ");
    scanf("%d", &choice);
    if (choice == 0)
    {
        printf("Enter the real part: ");
        scanf("%f", &complex1.real);
        printf("Enter the imaginary part: ");
        scanf("%f", &complex1.compl );
        printf("Enter the real part: ");
        scanf("%f", &complex2.real);
        printf("Enter the imaginary part: ");
        scanf("%f", &complex2.compl );
        // Division
        div = pow(complex2.real, 2) + pow(complex2.compl, 2);
        complex3.real = (complex1.real * complex2.real + complex1.compl *complex2.compl ) / div;
        complex3.compl = (complex1.compl *complex2.real - complex1.real * complex2.compl ) / div;
        complexdiv = PRecttoPolar(complex3);
    }
    else if (choice == 1)
    {
        printf("Enter the module: ");
        scanf("%f", &complex1.module);
        printf("Enter the argument: ");
        scanf("%f", &complex1.argument);
        printf("Enter the module: ");
        scanf("%f", &complex2.module);
        printf("Enter the argument: ");
        scanf("%f", &complex2.argument);
        // Division
        complex1 = PPolartoRect(complex1);
        complex2 = PPolartoRect(complex2);
        div = pow(complex2.real, 2) + pow(complex2.compl, 2);
        complex3.real = (complex1.real * complex2.real + complex1.compl *complex2.compl ) / div;
        complex3.compl = (complex1.compl *complex2.real - complex1.real * complex2.compl ) / div;
        complexdiv = PRecttoPolar(complex3);
    }
    else
    {
        printf("The format is not valid!");
    }
    printf("Real part: %f and Imaginary part: %f\n", complexdiv.real, complexdiv.compl );
    printf("Argument: %f and Module: %f\n", complexdiv.argument, complexdiv.module);
}

int main()
{
    printf("Exercice 1:\n");
    exercice1();
    printf("Exercice 2:\n");
    exercice2();
    printf("Exercice 3:\n");
    exercice3();
    printf("Exercice 4:\n");
    RecttoPolar();
    PolartoRect();
    SumCplx();
    SubCplx();
    MulCplx();
    DivCplx();
    return 0;
}
