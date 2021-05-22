#include <Arduino.h>
#include <ArduinoJson.h>
#include <Servo.h>

#define servoPin 9 // servo pin
Servo myservo;     // servo object

int limitSwitch = 3; // limit switch pin
char incomingByte;   // holds the byte from serial

int redPin = 5;
int yellowPin = 6;
int greenPin = 7;

boolean redLED = false;
boolean yellowLED = false;
boolean greenLED = false;

void lightLEDs()
{
  digitalWrite(redPin, redLED);
  digitalWrite(yellowPin, yellowLED);
  digitalWrite(greenPin, greenLED);
}

void checkFood()
{
  if (digitalRead(limitSwitch))
  {
    // if the limit switch is open, means nothing is holding it down
    redLED = false;
  }
  else
  {
    redLED = true;
  }
}

void dropFood()
{
  // if its feeding command, means catt has been seen
  greenLED = true;
  lightLEDs();

  // open servo
  myservo.write(40); // sets the servo position (0-180)
  delay(1000);
  myservo.write(112);

  greenLED = false;
  // now that we put food out, lets check its level
  checkFood();
  lightLEDs();
}

void setup()
{
  // put your setup code here, to run once:
  pinMode(limitSwitch, INPUT_PULLUP); // setups limit switch pin as input and pullups floating input
  // sets led pins as outputs
  pinMode(redPin, OUTPUT);
  pinMode(yellowPin, OUTPUT);
  pinMode(greenPin, OUTPUT);

  myservo.attach(servoPin); // attaches the servo on pin 9 to the servo object
  Serial.begin(9600);       // sets serial to run at a speed of 9600

  // on startup, check food level
  checkFood();
  lightLEDs();
  
  myservo.write(112); // sets the servo position (0-180)
}

void loop()
{
  // put your main code here, to run repeatedly:
  checkFood();
  lightLEDs();

  // if there is something in serial
  if (Serial.available() > 0)
  {
    // read the incoming byte:
    incomingByte = Serial.read();

    if (incomingByte == 't')
    {
      // t for TIME TO FEED (or maybe the opposite)
      yellowLED = !yellowLED;
      lightLEDs();
    }
    else if (incomingByte == 'p')
    {
      // if p, for "please feed me, IM HERE", servo needs to open, delay a bit, and go back
      dropFood();
    }
  }

  if (!redLED)
  {
    // if low food, constally spam f
    Serial.println('f');
  }
  else
  {
    // just spam o for "OH FUCK I HATE MY OWN SPAGHEITI CODE"
    Serial.println('o');
  }
}