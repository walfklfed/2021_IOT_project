#include <stdio.h>
#include <wiringPi.h>
#define RED 17
#define YELL 27
#define GREEN 22

int main (void)
{
    wiringPiSetupGpio();

    pinMode (RED, OUTPUT);
    pinMode (YELL, OUTPUT);
    pinMode (GREEN, OUTPUT);

    printf("Running...\n");
    for (int i=0; i<100; i++){
        printf("Red light on\n");
        digitalWrite (RED, HIGH); delay(1000);
        digitalWrite (RED,  LOW); delay(10);
        printf("Red light off\n");

        printf("Yellow light on\n");
        digitalWrite (YELL, HIGH); delay(10);
        digitalWrite (YELL,  LOW); delay(10);
        printf("Yellow light off\n");

        printf("Green light on\n");
        digitalWrite (GREEN, HIGH); delay(10);
        digitalWrite (GREEN,  LOW); delay(10);
        printf("Green light off\n");
    }
    printf("Finished!");
    return 0;
}