import serial
import time
from zlib import crc32

buffer = bytes()
anterior = 0
error = 0
contador = 0
s = serial.Serial("/dev/serial0")
s.baudrate = 115200

time0 = time.time()
s.reset_input_buffer()
while True:
#    print(s.in_waiting)
    if s.in_waiting >= 58:
        buffer = s.read(58)
#        print(buffer)
        data = buffer[:50]
        foreign_counter = buffer[50:54]
        foreign_counter_int = int.from_bytes(foreign_counter,"little")
        crc = buffer[54:]

        guess = crc32(data+foreign_counter).to_bytes(4, "little")
        if guess == crc: # no se ha liao
            print("{}: \tMensaje recibido correctamente".format(contador))
            if foreign_counter_int != contador:
                print("PAQUTES PERDIDOS: {}".format(foreign_counter_int-contador))
                contador = foreign_counter_int
        else:
            print("{}: \tERROR ERROR".format(contador))
        time0 = time.time()
        contador += 1
        buffer = bytes()

    else:
        pasado = time.time()-time0
        if s.in_waiting == 0:
            time0 = time.time() # resetear para que el timeout no salte cuando no se esta enviando nada (esto puede que sea un poquito pochingui)
        if pasado > 0.5:
            print("{}: \tTIMEOUT TIMEOUT".format(contador))
            s.reset_input_buffer()
            time0 = time.time()
