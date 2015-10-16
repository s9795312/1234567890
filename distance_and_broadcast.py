import pi2go, time
import communication

DIST_RUN = 40
DIST_STOP = 15
start = time.time()
dist = 50
state = "RUN"
prev_state = state

pi2go.init()

LEDon = 1024
LEDoff = 0

try:
	while True:
		if time.time() - start > 0.15:
			print "Starting distance measuring"
			dist = (int(pi2go.getDistance()*10))/10.0
			start = time.time()
			#print "Distance measuring finished"
		if dist > DIST_RUN:
			state = "RUN"
		elif dist > DIST_STOP:
			state = "WARN"
		else:
			state = "STOP"
			
		if state != prev_state:
			print state
			if state == "RUN":
				pi2go.setAllLEDs(LEDoff,LEDon,LEDoff)
			elif state == "WARN":
				pi2go.setAllLEDs(LEDon,LEDon,LEDoff)
			elif state == "STOP":
				pi2go.setAllLEDs(LEDon,LEDoff, LEDoff)
			else:
				print "unknown state!"
			#print time.time()
			#message = "State: " + state + " at " + str(time.time())
			print "Starting broadcast"
			for x in range(0,10):
				message = "    State: " + state + " at " + str(time.time()) + "#" + str(x)
				communication.send_broadcast_message(38234, message)
			#print time.time()
			print "Broadcast finished"
		prev_state = state
except KeyboardInterrupt:
	pass
finally:
	pi2go.cleanup()
		
				
	

