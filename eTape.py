from gpiozero import MCP3008
import time

resistor = 560

eTape = MCP3008(0)

# eTape.voltage
def readVoltage(eTape):
    #getting the ADC value
    adcValue = eTape.value
    # covert adcValue (analogValue) to a voltage (0-5V)
    # voltage = adcValue * (5.0/1023)
    voltage = (adcValue/1023)*5.0
    return voltage


while True:
    # # print(f'ADC Value: {eTape.value}')
    # # voltage = readVoltage(eTape)
    # # print(f'Voltage: {voltage}')
    # analogReading = eTape.value
    # print(f'Analog Reading: {analogReading}')
    # # covert value to resistance
    # # resistance = (1023.0 / analogReading) - 1.0
    # resistance = resistor / analogReading
    # print(f'Sensor output Resistance: {resistance} ohms')
    # volts = 5 * analogReading
    # print(f'volt {volts}')
    # print('\n')
    # time.sleep(5)

    adcReading = eTape.value
    print(f'ADC Reading: {adcReading}')
    volts = 5 * adcReading
    x = (1023.0 / 5.0) * volts
    print(f'x {x}')
    print('\n')
    time.sleep(5)










