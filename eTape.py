from gpiozero import MCP3008
import time

resistor = 560
eTape = MCP3008(0)
# TODO: Calibration is off need to re adjust
no_volume_resistance = 2086  # Resistance value (in ohms) when no liquid is present
calibration_resistance = 721  # Resistance value (in ohms) when liquid is at max line.
calibration_volume = 500.00


def main():
    while True:
        # water_level = water_level_percentage()
        # print(f'water level %: {water_level}')
        # print('\n')
        test_code()
        time.sleep(1)
        print("\n")


def read_resistance():
    reading = eTape.value * 1000
    # covert to resistance
    resist = (1023 / reading) - 1
    resist = resistor / resist
    print('resistance(): %.2f' % resist)


def resistance_to_volume():
    # TODO: Need to implement
    return 0


def water_level_percentage():
    ohms_value = eTape.value * 1000
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
    read_resistance()
    water_level_percentage(reading)


if __name__ == "__main__":
    main()
