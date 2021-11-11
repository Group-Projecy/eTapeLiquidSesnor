from gpiozero import MCP3008
import time

resistor = 560
eTape = MCP3008(0)
# TODO: Calibration is off need to re adjust
no_volume_resistance = 806.546  # Resistance value (in ohms) when no liquid is present
calibration_resistance = 463.582  # Resistance value (in ohms) when liquid is at max line.


def main():
    while True:
        # ohms_value = calculate_ohms_value(eTape)
        # water_level = water_level_prentage(ohms_value)
        # print(f'water level %: {water_level}')
        # print('\n')
        test_code()
        time.sleep(1)


def read_resistance():
    reading = eTape.value * 1000
    # covert to resistance
    resist = (1023 / reading) - 1
    resist = resistor / resist
    print(f'resistance: {resist}')


def water_level_prentage(ohms_value):
    percentage = (no_volume_resistance - ohms_value) / (no_volume_resistance - calibration_resistance)
    cm = 30 * percentage
    print(f'cm value: {cm}')
    return percentage


def test_code():
    reading = eTape.value * 1000
    print(f'adc: {reading}')
    # covert to resistance
    resist = (1023 / reading) - 1
    resist = resistor / resist
    print(f'resistance: {resist}')
    water_level_prentage(reading)


if __name__ == "__main__":
    main()
