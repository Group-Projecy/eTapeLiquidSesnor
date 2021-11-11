from gpiozero import MCP3008
import time

resistor = 560

eTape = MCP3008(0)


def readResistance(eTape,resistor):
    return 0


while True:
    analogReading = eTape.value
    print(f'Analog Reading: {analogReading}')
    # covert value from kohms  to ohms
    ohmsValue = analogReading * 1000
    print(f'ohms Vale {ohmsValue}')
    voltage = (5.0 / 1023) * ohmsValue
    print(f'voltage: {voltage}')
    print('\n')
    time.sleep(2)


# TODO double check code
# TODO my code is out putting kohms need to change to ohms
# https://hextobinary.com/unit/resistance/from/kohm/to/ohm









