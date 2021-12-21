#include <wiringPi.h>
#define LED 4

int main (void)
{
  //wiringPiSetup () ;
  wiringPiSetupGpio();
  pinMode (LED, OUTPUT) ;
  for (int i=0; i<1000; i++)
  {
    digitalWrite (LED, HIGH) ; delay (10) ;
    digitalWrite (LED,  LOW) ; delay (10) ;
  }
  return 0 ;
}