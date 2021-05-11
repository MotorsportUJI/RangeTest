import serial
import time
from zlib import crc32

# cada segundo se manda un payload de 64 bytes. COMPROBAR MAÑANA
payload = "01234567"*7 + "0123"
payload = payload.encode()
hashh = crc32(payload)
payload = payload + hashh.to_bytes(4, "little")

s = serial.Serial("/dev/ttyUSB0")


total_sent = 0
start_time = time.time()
counter = 0
while True:
    sent_count = s.write(payload)

    time.sleep(1)
    print(counter)
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