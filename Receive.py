import serial
import time
from zlib import crc32

buffer = bytes()
anterior = 0
error = 0
contador = 0
s = serial.Serial("/dev/ttyUSB0")
s.baudrate = 115200

time0 = time.time()
while True:
    if s.in_waiting >= 64:
        buffer = s.read(s.in_waiting)
        data = buffer[0:60]
        crc = buffer[60:65]

        guess = crc32(data).to_bytes(4, "little")
        if guess == crc: # no se ha liao
            print("{}: \tMensaje recibido correctamente".format(contador))
        else:
            print("{}: \tERROR ERROR".format(contador))
        time0 = time.time()
        contador += 1
        buffer = bytes()

    else:
        pasado = time.time()-time0
        if s.in_waiting == 0:
            time0 = time.time() # resetear para que el timeout no salte cuando no se esta enviando nada (esto puede que sea un poquito pochingui)
        if pasado > 0.2:
            print("{}: \tTIMEOUT TIMEOUT".format(contador))
            s.reset_input_buffer()
            time0 = time.time()