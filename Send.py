import serial
import time
from zlib import crc32

# cada segundo se manda un payload de 64 bytes. COMPROBAR MAÑANA
og = "01234567"*6+"01"
og = og.encode()
counter = 0
s = serial.Serial("/dev/ttyUSB0")
s.baudrate = 115200

total_sent = 0
start_time = time.time()
counter = 0
while True:
    print(counter)
    payload = og + counter.to_bytes(4,"little")
    tosent = payload + crc32(payload).to_bytes(4,"little")
    sent_count = s.write(tosent)
#    print(tosent)
    time.sleep(1)
    counter += 1
    
    """
    total_sent += sent_count
    time_expend = time.time()-start_time
    if time_expend > 1:
        counter += 1
        print("{0}:\tSpeed: {1:,} bytes/s".format(counter, round(total_sent/time_expend)))
        start_time = time.time()
        total_sent = 0
"""
