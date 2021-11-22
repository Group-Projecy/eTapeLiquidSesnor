from gpiozero import MCP3008
import time

resistor = 560      # Value of the series resistor in ohms
eTape = MCP3008(0)  # MCP pin the output is going to

no_volume_resistance = 2060  # Resistance value (in ohms) when no liquid is present
calibration_resistance = 485  # Resistance value (in ohms) when liquid is at max line.
calibration_volume = 30        # length of tape (cm0


def main():
    while True:
        test_code()
        time.sleep(1)
        print("\n")

def write_to_file(water_level):
    temp_readings_file = open("dataGathered-Etape.txt", "a")
    temp_readings_file.write('\ncm: '+water_level)
    temp_readings_file.close()


def read_resistance():
    reading = eTape.value * 1000
    # covert to resistance
    resist = (1023 / reading) - 1
    resist = resistor / resist
    print('resistance(): %.2f' % resist)
    return resist


def water_level(ohms_value):
    if ohms_value > no_volume_resistance or (no_volume_resistance - calibration_resistance) == 0.0:
        # if no max value for resistance is set
        return 0.0
    else:
        water_level_measurement = (no_volume_resistance - ohms_value) / (no_volume_resistance - calibration_resistance)
        cm = 30 * water_level_measurement
        return cm


def test_code():
    reading = eTape.value * 1000
    print(f'adc: {reading}')
    # ohms_value = resistance
    resistance = read_resistance()
    print("====================")
    cm_level = water_level(resistance)
    print(f'{cm_level} cm')


if __name__ == "__main__":
    main()
