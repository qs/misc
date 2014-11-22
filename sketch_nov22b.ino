#include <Wire.h>
#include "rgb_lcd.h"

rgb_lcd lcd;

int colorR = 200;
int colorG = 200;
int colorB = 200;

const int pinLight = A0;

void setup() 
{
    // set up the LCD's number of columns and rows:
    lcd.begin(16, 2);
    lcd.setRGB(colorR, colorG, colorB);
}

void loop() 
{
    colorR = random(10, 250);
    colorG = random(10, 250);
    colorB = random(10, 250);
    lcd.setRGB(colorR, colorG, colorB);
    lcd.print(HIGH);
    delay(200);
}
