#include <Servo.h>

Servo servomotor;


void setup(){
  Serial.begin(9600);
  servomotor.attach(9);
  
  
  }
  



void loop(){
  servomotor.write(0);
  delay(1000);
  servomotor.write(90);
  delay(1000);
  servomotor.write(180);
  delay(1000);
  }
