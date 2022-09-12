







import pyfirmata
import smtplib
import datetime

#FOR EMAIL
#sender_email="bishal.saha04052002@gmail.com"
#rec_email="sneha.harish2020@vitstudent.ac.in"
sender_email = "bishal.saha04052002@gmail.com"
rec_email = "hanumansaha.1975@gmail,com"
password="pzvohebisqnyxxky"
#message="Hey,This is Your Fellow Arduino UNO.I have turned ON Lights,OKKKKK.Arduino UNO..............."

#server=smtplib.SMTP('smtp.gmail.com',587)
#server.starttls()
#server.login(sender_email,password)






#FOR WHATSAPP
import pywhatkit
import time
import pyautogui

import keyboard as k




import pyfirmata
import smtplib
import datetime









#FOR WHATSAPP
import pywhatkit
import time
import pyautogui

import keyboard as k






import serial
ArduinoSerial=serial.Serial('COM5',9600)




def led2(val):
    if val==1:

        print("Hurray It is working.............................................................")
        print("Login Success")


    elif val==0:


        pywhatkit.sendwhatmsg('+917585848186','Hey...........,This is Your Fellow Arduino UNO.I have turned OFF Lights,OKKKKK.Arduino UNO...............Automate From Python',HOUR,MINUTE+2 , 30)
        pyautogui.click(1050, 950)

        k.press_and_release('enter')





def led(val):
    if val==1:

        print("Hurray It is working.............................................................")
        print("Login Success")
        #server.sendmail(sender_email, rec_email, message)
        #print("Email has been sent to", rec_email)

    elif val==0:



        k.press_and_release('enter')


while True:
    HOUR = datetime.datetime.now().hour  # the current hour
    MINUTE = datetime.datetime.now().minute  # the current minute
    print(HOUR, MINUTE)

    if(ArduinoSerial.inWaiting()>0):
        mydata=ArduinoSerial.readline()
        print(mydata)
        a=mydata.decode('UTF-8')
        print(type(a))
        if('25' in a):
            print("YES")
        res = [int(i) for i in mydata.split() if i.isdigit()]
        print(res)
        if(res[0]<24):
            print("temperature is too hot")



    a=int(input("Enter "))
    if(a==1):
        break
