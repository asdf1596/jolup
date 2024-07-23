#include <SoftwareSerial.h>

int led = 7;
int ENA = 11;
int IN1 = 10; 
int IN2 = 9;
int ENB = 6;
int IN3 = 5;
int IN4 = 4;
void setup() {
  // Serial.begin(9600);
  // // put your setup code here, to run once:
  // pinMode(led, OUTPUT);
  pinMode(ENA, OUTPUT); // 디지털 11번 핀을 출력(OUTPUT) 모드로 설정
    pinMode(IN1, OUTPUT);
    pinMode(IN2, OUTPUT);
    pinMode(ENB, OUTPUT);
    pinMode(IN3, OUTPUT);
    pinMode(IN4, OUTPUT);
}

void loop() {
  // while(Serial.available()>0){
  //   char c = Serial.read();
  //   if(c=='g'){
  //     digitalWrite(led,HIGH);
  //   }else if(c=='s'){
  //     digitalWrite(led,LOW);
  //   }
  // }
  digitalWrite(IN1, HIGH); 
  digitalWrite(IN2, LOW);
  analogWrite(ENA, 255);
  delay(1000);
  analogWrite(ENA, 0); 
  delay(1000);  
}
//왼 위:13,12,11(~)
//오 위:8,9,10(~)
//왼 아:7,6,5(~)
//오 아:4,2,3(~)