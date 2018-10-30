import RPi.GPIO as GPIO
import time
import smtplib

import datetime ##used to return the time of the break in


GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.IN)
GPIO.setup(24,GPIO.OUT)


GMAIL_USER= 'your gmail'
GMAIL_PASS= 'your password'
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587


##make a GUI for this ish

now=datetime.datetime.now()
text='Intruder alert. Motion detected at' + str(now)



while True:
    input_state = GPIO.input(18)
    if input_state == True:
        ## String to acknowledge the motion
        print('Motion Detected')

        ## Set off the alarm
       ## buzz(5000,20)
        
        ## send the email to the user
        send_email('pgrzyby@gmail.com,', 'INTRUDER ALERT!',text)
        time.sleep(120)

        ## insert what you actually want to be done when the motion is detected
    else:
        time.sleep(1) ##how often it checks the motion

##while True:
##    if GPIO.input(23): ##if there is a movement, PIR sensor gives input to GPIO 23
##        print("Motion detected")
##        GPIO.output(24,True) ##output given to buzzer
##        time.sleep(1) #buzzer turns on for 1 second
##        GPIO.output(24,False)
##        time.sleep(5)
##    time.sleep(0.1) 
##GPIO.cleanup()


def send_email(recipient, subject, text):
    smtpserver= smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(GMAIL_USER, GMAIL_PASS)
    header= 'To:' + recipient + '\n' + 'From: ' + GMAIL_USER
    header= header + '\n' + 'Subject:' + subject + '\n'
    msg = header + '\n' + text + '\n\n'
    smtpserver.sendmail(GMAIL_USER, recipient, msg)
    smtpserver.close()


def buzz(pitch,duration):
    period= 1.0/pitch
    delay= period/2
    cycles= int(duration *pitch)
    for i in range(cycles):
        GPIO.output(24, True)
        time.sleep(delay)
        GPIO.output(24, False)
        time.sleep(delay)





        

        

    

