#E-Tape Liquid Sensor
### Useful links for using the E-Tape:
[ETape Datasheet](https://cdn-shop.adafruit.com/datasheets/eTapeApp.pdf)

## Using the Sensor with a Pi:
The etape sensor output is Analogue and the pi GPIO pins are digital. We
have to use the MCP3008 that is ADC (Analogue-to-Digital converter).

### Configuring the pi to use mcp3008:
[Help for Circuit set-up & installs](https://projects.raspberrypi.org/en/projects/physical-computing/13)

On the Pi open a terminal window and install the spidev package
`sudo apt-get install python3-spidev python-spidev`

Enable SPI from the Raspberry Pi Configuration in Interfaces
`raspi-config`
