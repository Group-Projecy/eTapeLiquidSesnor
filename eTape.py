from gpiozero import MCP3008
import time

resistor = 560      # Value of the series resistor in ohms
eTape = MCP3008(0)  # MCP pin the output is going to

no_volume_resistance = 2086  # Resistance value (in ohms) when no liquid is present
calibration_resistance = 721  # Resistance value (in ohms) when liquid is at max line.
calibration_volume = 500.00


def main():
    while True:
        test_code()
        time.sleep(1)
        print("\n")


def read_resistance():
    reading = eTape.value * 1000
    # covert to resistance
    resist = (1023 / reading) - 1
    resist = resistor / resist
    print('resistance(): %.2f' % resist)
    return resist


def resistance_to_volume(resistance, zero_resistance, cal_resistance, cal_volume):
    if resistance > zero_resistance or (zero_resistance - cal_resistance) == 0.0:
        # if no max value for resistance is set
        return 0.0
    scale = (zero_resistance - resistance) / (zero_resistance - cal_resistance)
    return cal_volume * scale


def water_level_percentage():
    ohms_value = eTape.value * 1000
    percentage = (no_volume_resistance - ohms_value) / (no_volume_resistance - calibration_resistance)
    cm = 30 * percentage
    print(f'cm value: {cm}')
    return percentage


def test_code():
    reading = eTape.value * 1000
    print(f'adc: {reading}')
    # # covert to resistance
    # resist = (1023 / reading) - 1
    # resist = resistor / resist
    # print(f'resistance: {resist}')
    resistance = read_resistance()
    water_level_percentage(reading)
    print("====================")
    volume = resistance_to_volume(resistance, no_volume_resistance, calibration_resistance, calibration_volume)
    print(f'volume: {volume}')


if __name__ == "__main__":
    main()
