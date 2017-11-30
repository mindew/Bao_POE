#include <Servo.h>

Servo myservo;
int angle = 0;
int newAngle = 0;
// angle, or position of the servo
const int MaxChars = 4;
// limiting max characters of the serial monitor to be 4
// this array will be used to sent to PC via serial port
char strValue[MaxChars+1];
// length 20 is the maximum tolerance
int index = 0;
// initial value for index

void setup()
{
  Serial.begin(9600);
  //begin the serial monitor
  myservo.attach(9);
  // attach the servo at 9 (PWM)
  angle = 0;
  // initial servo set up: starting at 0 angle
}

void loop()
{}

// function serialEVent always listen
// when serial event is captured, this function activates
void serialEvent()
{
  // wait for the data to arrive
  while(Serial.available())
  {
    // fetch the serial value and overwrite it
    char ch = Serial.read();
    Serial.write(ch);

    if(index < MaxChars && isDigit(ch))
    {
      // if there is no data
      // stays same
      strValue[index++] = ch;
    }

    // if the streaming ended
    else
    {
      strValue[index] = 0;
      newAngle = atoi(strValue);
      // if there's any data
      // convert the string value to numeric value
      if (newAngle > 0 && newAngle < 180)
        if (newAngle < angle)
          for(; angle > newAngle; angle -= 1)
            {
            myservo.write(angle);
            // move the servo step by step backward
            }
        else
          for(; angle <newAngle; angle += 1)
          {
            myservo.write(angle);
            // move the servo step by step forward
          }
    }
    // reset the index and save the newAngle,
    // newAngle represents a new angle at which it must set the servo motor
    index = 0;
    angle = newAngle;
  }
}
