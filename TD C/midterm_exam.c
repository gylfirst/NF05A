// Midterm exam NF05A - TOURRETTE Matthieu
#include <stdio.h>

float add(float n1, float n2)
{
    float n3;
    n3 = n1 + n2;
    return n3;
}
float subtract(float n1, float n2)
{
    float n3;
    n3 = n1 - n2;
    return n3;
}
float multiply(float n1, float n2)
{
    float n3;
    n3 = n1 * n2;
    return n3;
}
float divide(float n1, float n2)
{
    float n3;
    n3 = n1 / n2;
    return n3;
}
int idivide(float n1, float n2)
{
    int n3;
    n3 = (int)n1 / (int)n2;
    return n3;
}
int modulo(float n1, float n2)
{
    int n3;
    n3 = (int)n1 % (int)n2;
    return n3;
}

int main()
{
    float n1, n2, n3;
    int n3i;
    char answer[10];
    do
    {
        printf("Enter the command (add, subtract, multiply, divide, idivide, modulo, and none to stop) and the 2 numbers: ");
        scanf("%s %f %f", answer, &n1, &n2);
        if (answer == "add")
        {
            n3 = add(n1, n2);
            printf("%f", n3);
        }
        else if (answer == "subtract")
        {
            n3 = subtract(n1, n2);
            printf("%f", n3);
        }
        else if (answer == "multiply")
        {
            n3 = multiply(n1, n2);
            printf("%f", n3);
        }
        else if (answer == "divide")
        {
            n3 = divide(n1, n2);
            printf("%f", n3);
        }
        else if (answer == "idivide")
        {
            n3i = idivide(n1, n2);
            printf("%d", n3i);
        }
        else if (answer == "modulo")
        {
            n3i = modulo(n1, n2);
            printf("%d", n3i);
        }
        else
            printf("Error: wrong command!\n");
    } while (answer != "none");
}
