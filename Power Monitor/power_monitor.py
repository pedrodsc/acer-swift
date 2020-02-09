#!/usr/bin/python

import re
import os

voltage_re = re.compile(r'(\d+.\d+) V')
current_re = re.compile(r'(\d+.\d+) (m?A)')

# Reference
# https://techbase.kde.org/Development/Tutorials/Sensors

# path
# /home/pedrovdsc/Projects/Power Plotter/power_plotter.py
if __name__ == '__main__':
    print('ksysguardd 1.2.0')
    while True:
        request = input('ksysguardd> ')

        stream = os.popen('sensors')
        output = stream.read()

        voltage_str = voltage_re.findall(output)[0]
        current_str, current_sufix = current_re.findall(output)[0]

        voltage = float(voltage_str)
        current = float(current_str) * (1 if 'm' in current_sufix else 1000)
        power = voltage * current / 1000

        if request == 'monitors':
            print('Voltage\tfloat')
            print('Current\tfloat')
            print('Power\tfloat')
        elif request == 'Voltage':
            print(voltage)
        elif request == 'Voltage?':
             print('voltage\t10\t14\tV')
        elif request == 'Current':
            print(current)
        elif request == 'Current?':
            print('current\t0\t3000\tmA')
        elif request == 'Power':
            print(power)
        elif request == 'Power?':
            print('power\t0\t45\tW')