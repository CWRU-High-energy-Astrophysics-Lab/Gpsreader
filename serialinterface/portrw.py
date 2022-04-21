import serial



port= serial.Serial('/dev/ttyUSB0')

response=[]
while True:
       next2byte=port.read(2)
       if b'@@'== next2byte:
           print(response)

           response=[]


       else:
           #print(next2byte.hex())
           response.append( next2byte.hex())