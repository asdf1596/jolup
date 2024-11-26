#include <SoftwareSerial.h>
#include <AFMotor.h>
#define BT_RXD 4 //hc06 TX to ArdUno D2
#define BT_TXD 5 //hc06 RX to ArdUno D3
AF_DCMotor motor_1(1);
AF_DCMotor motor_4(4);
SoftwareSerial hc06(BT_RXD, BT_TXD);

int TrigPin = A0;
int EchoPin = A1;
long duration, distance;
bool obstacleCheckFlag = false;  // Obstacle_Check()와 move()를 번갈아 실행하는 플래그
void Obstacle_Check();
void Distance_Measurement();
void move(char val);
void continuousMove(char val);

void setup() {
    hc06.begin(9600);
    Serial.begin(9600);
    motor_1.setSpeed(0);
    motor_1.run(RELEASE);
    motor_4.setSpeed(0);
    motor_4.run(RELEASE);
    pinMode(EchoPin, INPUT);  // EchoPin 입력
    pinMode(TrigPin, OUTPUT);
}

void loop() {
    char a = 'a';
    if (Serial.available()) {
        char val = Serial.read();
        a = val;
        while(a == val){
            Serial.println("asd");
            move(val);
            delay(50);
            val = Serial.read();
        }
        a = val;
    }
}

void move(char val) {
    switch (val) {
        case 'f':
            Serial.print(val);
            go_motor(170);
            break;
        case 'b':
            Serial.print(val);
            back_motor(170);
            break;
        case 'r':
            Serial.print(val);
            right_motor(150);
            break;
        case 'l':
            Serial.print(val);
            left_motor(150);
            break;
        case 's':
            Serial.print(val);
            stop_motor();
            break;
        default:
            Serial.print(val);
            stop_motor();
    }
}

void go_motor(uint8_t speedSet) {
    motor_1.setSpeed(speedSet);
    motor_4.setSpeed(speedSet);
    motor_1.run(FORWARD);
    motor_4.run(FORWARD);
}

void back_motor(uint8_t speedSet) {
    motor_1.setSpeed(speedSet);
    motor_4.setSpeed(speedSet);
    motor_1.run(BACKWARD);
    motor_4.run(BACKWARD);
}

void right_motor(uint8_t speedSet) {
    motor_1.setSpeed(speedSet);
    motor_4.setSpeed(speedSet);
    motor_1.run(BACKWARD);
    motor_4.run(FORWARD);
}

void left_motor(uint8_t speedSet) {
    motor_1.setSpeed(speedSet);
    motor_4.setSpeed(speedSet);
    motor_1.run(FORWARD);
    motor_4.run(BACKWARD);
}

void stop_motor() {
    motor_1.run(RELEASE);
    motor_4.run(RELEASE);
}
