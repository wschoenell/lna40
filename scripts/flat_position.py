import time
import sys
from chimera.core.manager import Manager


flat_tag = 902

m = Manager()

telescope = m.getProxy("192.168.56.1:7666/TheSkyTelescope/paramount")
print("Unparking telescope")
telescope.unpark()
#print("Homing telescope")
#telescope._findHome()

#raw_input("next..")

dome = m.getProxy("192.168.56.1:7666/DomeLNA/dome40")
print("Standing dome")
dome.stand()
print("Moving dome")
dome._command("MEADE DOMO MOVER = %03d" % flat_tag)

t0 = time.time()
while not dome._checkIdle():
    if time.time() - t0 > dome["slew_timeout"]:
        print("Error moving dome...")
        sys.exit(1)

print("Lights On")
dome.lightsOn()

raw_input("Press ENTER to finish and turn Lights Off")

print("Lights Off")
dome.lightsOff()