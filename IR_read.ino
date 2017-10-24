#include <Servo.h>
Servo servo;   // create servo object to control a servo

// Variables
const int sensorPin = A0;   // select the pin for IR sensor
int sensor = 0;             // define the class for the sensor value
float pos = 0;                  // position of the servo
float ratio = 180/1023;                // ratio of the sensor value and 180 degrees
// ratio is acquired by: 1023/180


void setup() {
  Serial.begin(9600);      // start serial monitor
  servo.attach(9);          // attaches the servo on pin 9
  }

  
void loop() {
  sensor = analogRead(sensorPin);     // read the IR sensor value
  Serial.println(sensor);
  delay(50);                           // waits 2 ms to settle the reading value
  pos = sensor * ratio;               // converts the sensor value to position degrees
  servo.write(pos);                   // tell servo to go to set position
}
