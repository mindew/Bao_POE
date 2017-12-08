  #include <Servo.h>
  
  const byte servoCount = 25;
  Servo servo[servoCount];
  
  const int initpos = 0;
  
  void setup(){
  Serial.begin(9600);
  Serial.println("Ready to go!");
  
  // attach servos
  servo[1].attach(22);
  servo[2].attach(23);
  servo[3].attach(24);
  servo[4].attach(25);
  servo[5].attach(26);
  servo[6].attach(27);
  servo[7].attach(28);
  servo[8].attach(29);
  servo[9].attach(30);
  servo[10].attach(31);
  servo[11].attach(32);
  servo[12].attach(33);
  servo[13].attach(34);
  servo[14].attach(35);
  servo[15].attach(36);
  servo[16].attach(37);
  servo[17].attach(38);
  servo[18].attach(39);
  servo[19].attach(40);
  servo[20].attach(41);
  servo[21].attach(42);
  servo[22].attach(43);
  servo[23].attach(44);
  servo[24].attach(45);
  servo[25].attach(46);

  
  }
  
  void loop(){
  byte index = 1;
  
  
  for (byte servoindex = 1; servoindex < servoCount; servoindex++)
  {
      servo[servoindex].write(initpos);
  }
  
  while(true)
  {
    if(Serial.available() > 0)
    {
      digitalWrite(13, !digitalRead(13));
      byte serv_pos = Serial.read();
      serv_pos = map(serv_pos, 0, 255, 0, 180);
      Serial.print(serv_pos);  
      Serial.print(", ");
      Serial.println(index);
      servo[index].write(serv_pos);
      
      index = index + 1;
      
      }  
    }
  }

