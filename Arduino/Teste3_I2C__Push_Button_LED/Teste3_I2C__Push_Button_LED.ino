
//ACENDE LED I2C 
//Código retirado de https://oscarliang.com/raspberry-pi-arduino-connected-i2c/


#include "Wire.h"

#define SLAVE_ADDRESS 0x04
int number = 0;
int state = 0;
int data = 0;

void setup() {
  pinMode(13, OUTPUT);
  Serial.begin(9600); // start serial for output
  // initialize i2c as slave
  Wire.begin(SLAVE_ADDRESS);
  
  // define callbacks for i2c communication
  Wire.onReceive(receiveData);
  Wire.onRequest(sendData);
  
  Serial.println("Ready!");
}

void loop() {
  /*
  state = digitalRead(12);
  if (state == HIGH){
    data = 0x1;                                 
  }
  else {
    data = 0x0;
  }
  Wire.beginTransmission(SLAVE_AD);
  Wire.write(0x1);
  Wire.endTransmission(4);
  Serial.print("Data sent: ");
  Serial.println(data);
*/
  delay(100);
  
}

// callback for received data

void receiveData(int byteCount){

  while(Wire.available()) {
      number = Wire.read();
      if (number == 0x1){
          digitalWrite(13, HIGH);
          delay(1000);
      }
      else if (number == 0x0){
          digitalWrite(13, LOW);
          delay(1000);
      }
      /*
      if (state == 0){
         // set the LED on
        state = 1;
      } else {
        digitalWrite(13, LOW); // set the LED off
        state = 0;
      }
      */
      Serial.print("Data received: ");
      Serial.println(number);
    }
    
    
    
  }


// callback for sending data
void sendData(){
  state = digitalRead(12);
  if (state == HIGH){
    data = 0x1;                                 
  }
  else {
    data = 0x0;
  }
  Wire.write(data);
  Serial.print("Data was requested.");
  Serial.print("Data sent: ");
  Serial.println(data);
  delay(100);
}
