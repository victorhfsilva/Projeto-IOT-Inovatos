#include <Wire.h>

#define SLAVE_ADDRESS 0x4

const int buttonPin = 12;
const int ledPin = 13;

int i2c_received_data = 0;
int button_state = 0;
int data = 0;

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
  while(Wire.available()){
    i2c_received_data = Wire.read();
    if (i2c_received_data == 0x1){
          digitalWrite(ledPin, HIGH);
          delay(100);
    }
    else if (i2c_received_data == 0x0){
          digitalWrite(ledPin, LOW);
          delay(100);
    }
    Serial.print("Data received: ");
    Serial.println(i2c_received_data);
  }
}

void sendData(){
  button_state = digitalRead(buttonPin);
  if (button_state == HIGH){
    data = 0x1;                                 
  }
  else {
    data = 0x0;
  }
  Wire.write(data);
  Serial.print("Data sent: ");
  Serial.println(data);
  delay(100);
}
