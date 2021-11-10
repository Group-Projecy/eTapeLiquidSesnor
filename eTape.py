# https://learn.adafruit.com/smart-measuring-cup?view=all - Helped
from gpiozero import MCP3008
import time

resistor = 560

eTape = MCP3008(0)


def readVoltage(eTape):
    #getting the ADC value
    adcValue = eTape.value
    # covert adcValue (analogValue) to a voltage (0-5V)
    voltage = adcValue * (5.0/1023)
    return voltage


while True:
    print(f'ADC Value: {eTape.value}')
    voltage = readVoltage(eTape)
    print(f'Voltage: {voltage}')
    time.sleep(5)








