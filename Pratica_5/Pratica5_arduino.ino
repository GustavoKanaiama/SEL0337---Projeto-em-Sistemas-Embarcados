#include <Wire.h>

const int ledPin = LED_BUILTIN;

int varRead = 0;
int highB = 0;
int lowB = 0;

void setup() {
 
  Serial.begin(9600);
  Wire.onRequest(requestEvent);
 
  //------
 
  Wire.begin(0x8);
 
  Wire.onReceive(receiveEvent);
 
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, LOW);
}

void requestEvent(){
  varRead = analogRead(A0);
  Serial.println(varRead);
  highB = highByte(varRead);
  lowB = lowByte(varRead);
 
  Wire.write(highB);
  Wire.write(lowB);
 
}


void receiveEvent(int howMany){
 while (Wire.available()){
   char c = Wire.read();
   digitalWrite(ledPin, c);
 }
 
}  

void loop() {
  
  varRead = analogRead(A0);
  Serial.println(varRead);
  highB = highByte(varRead);
  lowB = lowByte(varRead);

  delay(100);
}