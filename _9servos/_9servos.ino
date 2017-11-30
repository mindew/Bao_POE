#include <Servo.h>

const byte servoCount = 25;
Servo servo[servoCount];

const int initpos = 0;

void setup(){
  Serial.begin(9600);
  Serial.println("Ready to go!");
  
  // attach servos
  servo[0].attach(22);
  servo[1].attach(23);
  servo[2].attach(24);
  servo[3].attach(25);
  servo[4].attach(26);
  servo[5].attach(27);
  servo[6].attach(28);
  servo[7].attach(29);
  servo[8].attach(30);
  servo[9].attach(31);
  servo[10].attach(32);
  servo[11].attach(33);
  servo[12].attach(34);
  servo[13].attach(35);
  servo[14].attach(36);
  servo[15].attach(37);
  servo[16].attach(38);
  servo[17].attach(39);
  servo[18].attach(40);
  servo[19].attach(41);
  servo[20].attach(42);
  servo[21].attach(43);
  servo[22].attach(44);
  servo[23].attach(45);
  servo[24].attach(46);

  // initialize servo's position
  for (byte servoindex = 0; servoindex < servoCount; servoindex = servoindex + 1){
    servo[servoindex].write(initpos);
  }
}

void loop(){
  int serv_pos[3];
  byte index = 0;
  
  if(Serial.available() > 0){
    int serv_pos = Serial.read();
      Serial.println(serv_pos, DEC);
      if (Serial.read() == '\n') 
      {index = index + 1;
      }
//      if(serv_pos == 10) //ASCII for line feed
//      {
//       index = index + 1;
//     }  
     
     servo[index].write(serv_pos);
     
     delay(10); // wait until things settle down
   }
}
