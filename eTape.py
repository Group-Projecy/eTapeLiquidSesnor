from gpiozero import MCP3008
import time

resistor = 560
eTape = MCP3008(0)

no_volume_resistance = 806.546  # Resistance value (in ohms) when no liquid is present
calibration_resistance = 463.582  # Resistance value (in ohms) when liquid is at max line.


def ohmsValue(eTape):
    analogReading = eTape.value
    # covert value from kohms  to ohms
    ohmsValue = analogReading * 1000
    return ohmsValue


def waterLevelPrentage(ohmsValue):
    precentage = (no_volume_resistance - ohmsValue) / (no_volume_resistance - calibration_resistance)
    cm = 30 * precentage
    print(f'cm value: {cm}')
    return precentage


while True:
    ohmsValue = ohmsValue(eTape)
    waterLevel = waterLevelPrentage(ohmsValue)
    print(f'water level %: {waterLevel}')
    print('\n')
    time.sleep(2)

