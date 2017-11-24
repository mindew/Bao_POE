#include <Servo.h>

Servo servo1; 
Servo servo2;
Servo servo3;
Servo servo4;
Servo servo5;
Servo servo6;
Servo servo7;
Servo servo8;
Servo servo9;

int servo1pin =  2;
int servo2pin =  3;
int servo3pin =  4;
int servo4pin =  5;
int servo5pin =  6;
int servo6pin =  7;
int servo7pin =  8;
int servo8pin =  9;
int servo9pin =  10;

unsigned long previousMillis = 0;        // will store last time 
long time1 = 2000;           // milliseconds
long time2 = 10000;

char init_positions[]={0,0,0,0,0,0,0,0,0};
int positions[]={90,90,90,90,90,90,90,90,90};

void setup(){
  Serial.begin(9600);
  servo1.attach(servo1pin);
  servo2.attach(servo2pin);
  servo3.attach(servo3pin);
  servo4.attach(servo4pin);
  servo5.attach(servo5pin);
  servo6.attach(servo6pin);
  servo7.attach(servo7pin);
  servo8.attach(servo8pin);
  servo9.attach(servo9pin);
  
  servo1.write(0);
  servo2.write(0);
  servo3.write(0);
  servo4.write(0);
  servo5.write(0);
  servo6.write(0);
  servo7.write(0);
  servo8.write(0);
  servo9.write(0);
}
 
void loop(){
  unsigned long currentMillis = millis();
  if((currentMillis - previousMillis >= time1)){
    servo1.write(30);
    servo2.write(100);
    servo3.write(30);
    servo4.write(100);
    servo5.write(180);
    servo6.write(100);
    servo7.write(30);
    servo8.write(100);
    servo9.write(30);

    previousMillis = currentMillis;
  }

}

