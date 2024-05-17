int led = 7;
void setup() {
  Serial.begin(9600);
  // put your setup code here, to run once:
  pinMode(led, OUTPUT);
}

void loop() {
  while(Serial.available()>0){
    char c = Serial.read();
    if(c=='g'){
      digitalWrite(led,HIGH);
    }else if(c=='s'){
      digitalWrite(led,LOW);
    }
  }
}