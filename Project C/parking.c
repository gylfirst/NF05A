#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <iso646.h>
#include <string.h>

/// Generates a file if there isn't one
///
/// This function first checks if there is a .txt file to save the reservation of car slots.
/// \n If there isn't it creates one where each slot is randomly assigned 0 or 1 (available or not available).

void generatefile()
{
    FILE *file = fopen("availability.txt", "r");
    if (file == NULL)
    {
        FILE *fptr = fopen("availability.txt", "w");
        int a;
        for (int i = 0; i < 100; i++)
        {
            a = (rand() % 2);
            fprintf(fptr, "%d:%d\n", i + 1, a);
        }
        fclose(fptr);
    }
    else
        fclose(file);
}

/// Change the state of a slot from available to not available
/// @param slot Number of the slot you want to reserve.
///
/// Open the .txt file and goes to the slot given in parameter.
/// \n It then changes the value from 0 to 1 (available to not available) to reserve it.

void reservation(int slot)
{
    FILE *fptr = fopen("availability.txt", "r+");
    int c, tmp, linecount = 1;
    while ((c = fgetc(fptr)) != EOF)
    {
        if (c == '\n')
            linecount++;
        if (linecount == slot)
            break;
    }
    fscanf(fptr, "%d", &tmp);
    fseek(fptr, 1, SEEK_CUR);
    fprintf(fptr, "%d", 1);
    fclose(fptr);
}

/// Checks if a slot is available
/// @param slot Number of the slot you want to check.
/// @return Return 0 (available) or 1 (not available).
///
/// Open the .txt file and goes to the slot given in parameter.
/// \n It then takes the value associated to the slot (0 or 1) and returns it.

int checkavailability(int slot)
{
    FILE *file = fopen("availability.txt", "r");
    int n, c, linecount = 1;
    while ((c = fgetc(file)) != EOF)
    {
        if (c == '\n')
            linecount++;
        if (linecount == slot)
            break;
    }
    fscanf(file, "%d", &n);
    fseek(file, 1, SEEK_CUR);
    fscanf(file, "%d", &n);
    fclose(file);
    return n;
}

/// Asks a slot number and returns the availability
///
/// It asks the user to enter a car slot number, verifies if it exists. If not it asks the user again.
/// \n Afterwards it calls the function checkavailability() with the car slot and prints Available if it is returned 0 or Not available otherwise.
/// @see checkavailability()

void case1()
{
    int n = 0;
    while (n < 1 or n > 100)
    {
        printf("Enter the number of the car slot you want to check\n");
        scanf("%d", &n);
        if (n < 1 or n > 100)
            printf("The car slot doesn't exist\n");
    }
    int check = checkavailability(n);
    if (check == 1)
        printf("Not Available\n");
    else
        printf("Available\n");
}

/// Prints all the available slots
///
/// Calls the checkavailability() function for the number of slots the parking has (here 100).
/// \n Each time, it checks if it's available. If it is, it prints the slot number. Otherwise it goes to the next slot.
/// @see checkavailability()

void case2()
{
    printf("The available car slots are :\n");
    for (int i = 0; i < 100; i++)
    {
        if (checkavailability(i + 1) == 0)
            printf("%d\n", i + 1);
    }
}

/// Prints the number of available slots
///
/// Calls the checkavailability() function for the number of slots the parking has (here 100).
/// \n Each time, it checks if it's available. If it is, it adds 1 to a compter. Otherwise it goes to the next slot.
/// \n Finally it prints the number of slots available.
/// @see checkavailability()

void case3()
{
    int nb = 0;
    for (int i = 0; i < 100; i++)
    {
        if (checkavailability(i + 1) == 0)
            nb++;
    }
    printf("The are %d available car slots\n", nb);
}

/// It reserves the slot the user input.
///
/// Check if the slot imput by the user is available ot not. If not it asks the user again. Otherwise, the program change the value to not available.
/// \n It prints the confirmation if it has worked.
/// @see checkavailability() reservation()

void case4()
{
    int n;
    do
    {
        n = 0;
        while (n < 1 or n > 100)
        {
            printf("Enter the number of the car slot you want to reserve\n");
            scanf("%d", &n);
            if (n < 1 or n > 100)
                printf("The car slot doesn't exist\n");
        }
        if (checkavailability(n) == 1)
            printf("Sorry, this slot is not available right now\n");
    } while (checkavailability(n) == 1);
    reservation(n);
    printf("Your slot is well reserved\n");
}

/// Main function of the program.
/// @return 0 if the program is executed without problem
///
/// Calls the function based on the user's choice through a menu.
/// \n The program will run until the user makes a reservation.
/// @see generatefile() case1() case2() case3() case4()

int main()
{
    generatefile();
    int choice;
    printf("Hello and welcome to the smart parking reservation system !\n");
    do
    {
        choice = 0;
        while (choice < 1 or choice > 4)
        {
            printf("Choose one of the following options by entering 1, 2, 3 or 4\n");
            printf("1-Check the availability of a specific car slot\n");
            printf("2-Display all available car slots\n");
            printf("3-Display the number of available car slots\n");
            printf("4-Make a reservation\n");
            scanf("%d", &choice);
            system("cls"); // clear console

            switch (choice)
            {
            case 1:
                case1();
                break;
            case 2:
                case2();
                break;
            case 3:
                case3();
                break;
            case 4:
                case4();
                break;
            default:
                printf("Incorrect number\n");
            }
            printf("\n");
        }
    } while (choice != 4);
    printf("Press ENTER one time to terminate the program");
    getchar();
    getchar();
    return 0;
}
