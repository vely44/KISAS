from gpiozero import LED
from gpiozero import PWMLED
from gpiozero import Button
from time import sleep

led3 = LED(13)
led2 = LED(19)
led1 = LED(26)
led4 = LED(6)
led5 = LED(5)
button4 = Button(21)
button3 = Button(20)
button2 = Button(16)

def allon():
    led1.on()
    led2.on()
    led3.on()
    led4.on()
    led5.on()
    
def alloff():
    led1.off()
    led2.off()
    led3.off()
    led4.off()
    led5.off()


def alarm():
    allon()
    sleep(0.5)
    alloff()
    sleep(0.5)
    allon()
    sleep(0.5)
    alloff()
    sleep(0.5)
    allon()
    sleep(0.5)
    alloff()
    sleep(0.5)
    allon()
    sleep(0.5)
    alloff()
    sleep(0.5)
    allon()
    sleep(0.5)
    alloff()
    sleep(0.5)
    allon()
    sleep(0.5)
    alloff()
    sleep(0.5)

print("Mail Sender")
allon()
alarm()
sleep(1)
print("SMTP")
print("G-Mail Server")
alloff()
sleep(1)
print("Connected")
print("...")
sleep(1)
led1.on()
print("...")
sleep(1)
print("...")
sleep(1)
print("...")
sleep(1)
print("Hello, My name is MailBot.")
sleep(1)
print("I can send emails for you.")
sleep(1)
print("Let me show you.")
sleep(1)
sleep(1)
name=input("What is your name?")
print("Oooo, nice to meet you", name,"!")
sleep(1)
led2.on()
print("So", name, " let's send an email.")
sleep(1)
print("Your email should have a title.")
sleep(1)
title=input("Title:")
sleep(1)
led3.on()
print("Ok, Now write something in the body of the email.")
sleep(1)
body=input("Body:")
print("Thank you!")
sleep(1)
led4.on()
print("I will put them together.")
sleep(1)
print("...")
sleep(1)
print("...")
sleep(1)
print("Done!")
sleep(1)
print("Your email looks like this now:")
print("...............................")
print("Title:")
print(title)
print("Body:")
print(body)
print("...............................")
print("End")
sleep(1)
print("The email is almost ready now. The address is missing.")
sleep(1)
print("I'll put a random one...:))")
sleep(1)
address=input("Address please:")
print("Ok, so now is ready.")
sleep(1)
led5.on()

print("Your email looks like this now:")
print("Address:")
print(address)
print("...............................")
print("Title:")
print(title)
print("Body:")
print(body)
print("...............................")
print("End")
sleep(1)

print("In order for me to send the email, there is one more step.")
sleep(1)
print("...")
sleep(1)
print("...")
sleep(1)
print("We need to confirm the transaction.")
alarm()
sleep(1)
print("We will use a button for this.")
print("...")
print("Now press the SECRET button for the...")
sleep(5)
button3.wait_for_press()
alarm()
print("MAGIC to work.")
alarm()
sleep(1)


import subprocess
e = 'echo '+str(body)+' | mail -s '+str(title)+' '+str(address)
subprocess.call(e,shell=True)


print("Done!")

alloff()
