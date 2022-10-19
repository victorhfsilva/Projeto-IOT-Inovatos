#include "Wire.h"

#define SLAVE_ADDRESS 0x04

const int buttonPin = 12;
const int ledPin = 13;
int i2c_received_data = 0;
int button_state = 0;

void setup() {
  pinMode(ledPin, OUTPUT);
  pinMode(buttonPin, INPUT);
 
  Wire.begin(SLAVE_ADDRESS);
  Wire.onReceive(receiveData);
  Wire.onRequest(sendData);
}

void loop() {
      
  delay(100);
}

void receiveData(int byteCount){
  while (Wire.available()){
    if (i2c_received_data == 1){
      digitalWrite(ledPin, HIGH);
    }
  }
}

void sendData(){
  button_state = digitalRead(buttonPin);
  if (button_state == HIGH){
    Wire.beginTransmission(4);
    Wire.write(1);
    Wire.endTransmission();
  }
}
