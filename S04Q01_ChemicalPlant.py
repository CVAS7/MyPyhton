"""
 A Chemical plant has a tank for storing ethanol.
            - When the tank is more than 80% full, it
                 should raise an alarm to close the valve.
            - When the tank is less than 20% full, it
                 should send an SMS to buy more liquid.
            - The total tank capacity is 900 litres.
            - Write a program to simulate this.
            - Ask user to enter current level of ethanol in the tank.
            - Print the appropriate action based on value entered
            - Make sure that your program needs minimum changes
                 for a tank of different capacity."""
import os
import boto3

def beep():
    os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (5, 340))

def sms():
    client = boto3.client('sns')
    client = boto3.client('sns', 'us-west-2')
    client.publish(PhoneNumber='+919620444407', Message='You need to buy more liquid')

def CapCheck(n1,n2):
    p = float((n1/n2)*100)
    if p >= 80.0:
        print ("Your Current % of Liquid in tank is", round(p,2))
        print ("You need to close the valve")
        beep()
    elif p <= 20.0:
        print ("Your Current % of Liquid in tank is", round(p,2))
        print ("You need to buy more liquid")
        sms()
    else:
        print ("Your Current % of Liquid in tank is", round(p,2))
        print ("Your Tank level are in 20 to 80 %")

# Main
n1 = raw_input("Enter the current reading:")
CapCheck(int(n1),n2=900.0)
