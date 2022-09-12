import serial
ArduinoSerial=serial.Serial('COM5',9600)

while True:
    if(ArduinoSerial.inWaiting()>0):
        mydata=ArduinoSerial.readline()
        print(mydata)
        a=mydata.decode('UTF-8')
        print(type(a))
        if('25' in a):
            print("YES")
        res = [int(i) for i in mydata.split() if i.isdigit()]
        print(res)
        if(res[0]>25):
            print("temperature is Too hot")
    a=int(input("Enter "))
    if(a==1):
        break