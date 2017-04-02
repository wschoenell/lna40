import time
import requests

r = requests.post('http://200.131.64.143/login.html', data = dict(pw="Chimera065"))
#print r.text
r = requests.post('http://200.131.64.143/', data = dict(cte3="0"))
#print r.text
#raw_input("camera_off")
print "Camera power is OFF. Waiting 20s to power on."
time.sleep(20)
r = requests.post('http://200.131.64.143/', data = dict(cte3="1"))
print "Camera power is ON. Waiting 30s. Waiting 60s to start chimera"
time.sleep(30)
#print r.text
#raw_input("camera_on")