#!/usr/bin/env python3

import minimalmodbus
import time
from collections import namedtuple 

instr = minimalmodbus.Instrument("/dev/ttyUSB0", 3)
instr.serial.baudrate = 38400

Frame = namedtuple("Frame", ["cnt", "err", "unk", "sys", "i_v", "util", "o_v", "watt"])

def pack_frame(data):
    fr = Frame(
            cnt = data[0] >> 8,
            err = data[0] & 0xFF,
            unk = data[1] >> 12,
            sys = (data[1] >> 8) & 0xF,
            i_v = (((data[1] & 0xFF) << 4) + (data[2] >> 12)),
            util = data[2] >> 8 & 0xF,
            o_v = data[2] & 0xFF,
            watt = data[3]
            )
    return fr

last_count = 0

while True:
    f = pack_frame(instr.read_registers(0, 4, functioncode=4))

    if (f.cnt != last_count):
        last_count = f.cnt
        print(f)

    time.sleep(0.3)


