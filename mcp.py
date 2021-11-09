#getting the mcp to convert analog to digital first as the the etape outputs analog
#then put both codes together
from gpiozero import MCP3008

pot = MCP3008(0)

while True:
    print(pot.value)

