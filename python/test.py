from serial import Serial

arduino = Serial(

    port='COM5',
    baudrate=9600,
)
while(1):
    c = input()
    if(c == 'q'):
        break
    else:
        c = c.encode('utf-8')
        arduino.write(c)