unsigned int elapsed;
float t1,t2,t3,t4 = 0;
String message = "";
byte averages = 15;
int delay_time = 100; // default delay

void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT);
  digitalWrite(13, LOW);
  delay(500);
  digitalWrite(13, HIGH);

  delay_time = (900/averages);
}

void loop() {
  elapsed += 1;

  for (int i=0; i < averages; i++){
    t1 += analogRead(A0);
    t2 += analogRead(A1);
    t3 += analogRead(A2);
    t4 += analogRead(A3);
    delay(delay_time);
  }

  t1 /= float(averages);
  t2 /= float(averages);
  t3 /= float(averages);
  t4 /= float(averages);


  t1 = volt_to_temp(t1);
  t2 = volt_to_temp(t2);
  t3 = volt_to_temp(t3);
  t4 = volt_to_temp(t4);

  message = String(elapsed) + " " + String(t1,2) + " " + String(t2,2) + " " + String(t3,2) + " " + String(t4,2);
  Serial.println(message);
  
  
  t1 = t2 = t3 = t4 = 0;
 
  
  delay(50);
  
}


double volt_to_temp(float a_in){
  float resistance = (500000.0/((5*a_in)/1023)) - 100000.0;
  double temp = -4.107*pow(10,-35)*pow(resistance, 7) + 5.219*pow(10,-29)*pow(resistance, 6) - 2.681*pow(10,-23)*pow(resistance, 5) + 7.149*pow(10,-18)*pow(resistance, 4) 
  - 1.061*pow(10,-12)*pow(resistance, 3) + 8.823*pow(10,-8)*pow(resistance, 2) - 0.004115*resistance + 121.4;

  return temp;
}
