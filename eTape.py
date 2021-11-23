from gpiozero import MCP3008
import time

resistor = 560      # Value of the series resistor in ohms
eTape = MCP3008(0)  # MCP pin the output is going to

no_volume_resistance = 2060  # Resistance value (in ohms) when no liquid is present
calibration_resistance = 485  # Resistance value (in ohms) when liquid is at max line.
calibration_volume = 30        # length of tape (cm0

from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNStatusCategory, PNOperationType
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub


def main():
    while True:
        test_code()
        time.sleep(1)
        print("\n")


def write_to_file(water_level):
    temp_readings_file = open("dataGathered-Etape.txt", "a")
    temp_readings_file.write('\nWaterLevel: {0:0.0f} cm'.format(water_level))
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
    # elif ohms_value > calibration_resistance:
    #     # TODO if over max resistance = tank full
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
    print('WaterLevel: {0:0.1f} cm'.format(cm_level))
    print('WaterLevel: {0:0.0f} cm'.format(cm_level))


if __name__ == "__main__":
    main()
