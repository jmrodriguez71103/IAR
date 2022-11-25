 

<Servo.h> 
 

String pos;

int e = 0; 

Servo servo; 
 

void setup() {

  Serial.begin(9600); 

  servo.attach(9); 

}
 

void loop() {

  if(Serial.available()>=1){; 

  pos = Serial.readString();

  e= pos.toInt();

  servo.write(e); 

  delay(15); 

  }

}​