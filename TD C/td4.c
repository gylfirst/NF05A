// TD4 by Matthieu TOURRETTE TC02 in NF05A - UTT
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>

// Exercice 1:

float *in_vector(int N)
{
    int i;
    float *vector;
    vector = calloc(N, sizeof(float));
    for (i = 0; i < N; i++)
    {
        printf("Enter the value of the %dth element: ", i + 1);
        scanf("%f", (vector + i));
    }
    return vector;
}

float *sum_vector(float *vect1, float *vect2, int N)
{
    float *vectsum;
    vectsum = calloc(N, sizeof(float));
    for (int i = 0; i < N; i++)
    {
        vectsum[i] = vect1[i] + vect2[i];
    }
    return vectsum;
}

float *sub_vector(float *vect1, float *vect2, int N)
{
    float *vectsub;
    vectsub = calloc(N, sizeof(float));
    for (int i = 0; i < N; i++)
    {
        vectsub[i] = vect1[i] - vect2[i];
    }
    return vectsub;
}

float scal_vector(float *vect1, float *vect2, int N)
{
    float vect_scal;
    for (int i = 0; i < N; i++)
    {
        vect_scal += vect1[i] * vect2[i];
    }
    return vect_scal;
}

void print_vect(float *vector, int N)
{
    printf("Print of the vector:\n");
    for (int i = 0; i < N; i++)
    {
        printf("The value of the %dth element is: %f\n", i + 1, *(vector + i));
    }
}

int main()
{
    float *v1;
    float *v2;
    float *vectsum;
    float *vectsub;
    float scal;
    int N;
    printf("Enter the value of N: ");
    scanf("%d", &N);
    v1 = in_vector(N);
    v2 = in_vector(N);
    vectsum = sum_vector(v1, v2, N);
    vectsub = sub_vector(v1, v2, N);
    scal = scal_vector(v1, v2, N);
    print_vect(vectsum, N);
    print_vect(vectsub, N);
    printf("The scalar product of these vector is: %f\n", scal);
    return 0;
}

// Exercice 2:
struct Student
{
    char First_name[25];
    char Last_name[25];
    float Midterm_exam_grade;
    float Final_exam_grade;
    float Average_grade;
};
typedef struct Student Student;

// Average_grade = 0.4*Midterm + 0.6*Final

Student *in_array(int N)
{
    Student *list_stud = NULL;
    list_stud = malloc(N * sizeof(Student));
    for (int i = 0; i < N; i++)
    {
        printf("Student number %d\n", i + 1);
        printf("Enter the first name: ");
        scanf("%s", list_stud[i].First_name);
        printf("Enter the last name: ");
        scanf("%s", list_stud[i].Last_name);
        printf("Enter the midterm exam grade: ");
        scanf("%f", &list_stud[i].Midterm_exam_grade);
        printf("Enter the final exam grade: ");
        scanf("%f", &list_stud[i].Final_exam_grade);
        list_stud[i].Average_grade = 0.4 * list_stud[i].Midterm_exam_grade + 0.6 * list_stud[i].Final_exam_grade;
    }
    return list_stud;
}

void print_list(Student *list, int N)
{
    printf("Print of the list of students:\n");
    for (int i = 0; i < N; i++)
    {
        printf("Student number %d\n", i + 1);
        printf("The first name: %s\n", list[i].First_name);
        printf("The last name: %s\n", list[i].Last_name);
        printf("The midterm exam grade: %f\n", list[i].Midterm_exam_grade);
        printf("The final exam grade: %f\n", list[i].Final_exam_grade);
        printf("The average grade: %f\n\n", list[i].Average_grade);
    }
}

Student *sort_name(Student *list, int N)
{
    char inter[25];
    float intern = 0;
    int compt = 0;
    printf("Print of the list of students sorted by name:\n");
    while (compt < N)
    {
        for (int i = 0; i < N; i++)
        {
            if (list[i].First_name[0] > list[i + 1].First_name[0])
            {
                strcpy(inter, list[i + 1].First_name);
                strcpy(list[i + 1].First_name, list[i].First_name);
                strcpy(list[i].First_name, inter);
            }
        }
        compt++;
    }
    return list;
}

int main()
{
    int N;
    Student *list;
    Student *list_sn;
    printf("Enter the number of students: ");
    scanf("%d", &N);
    list = in_array(N);
    list_sn = sort_name(list, N);
    print_list(list, N);
    print_list(list_sn, N);
}
