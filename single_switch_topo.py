__author__ = 'Rakesh Kumar'

import time
import os
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.node import OVSSwitch
from mininet.topo import SingleSwitchTopo

class MininetMan():

    def __init__(self, controller_port):

        self.net = None
        self.controller_port = int(controller_port)

    def setup_mininet(self):


        self.net = Mininet(topo=SingleSwitchTopo(2),
                           autoStaticArp=True,
                           autoSetMacs=True,
                           controller=lambda name: RemoteController(name, ip='127.0.0.1', port=self.controller_port),
                           switch=OVSSwitch)

        # Start
        self.net.start()

		
	# Start a ping every 10 seconds
	try:
    		while True:
			h1 = self.net.getNodeByName("h1")
			h2 = self.net.getNodeByName("h2")

			#self.net.ping(hosts=[h1, h2])
			self.net.iperf(hosts=[h1, h2], seconds=1)
			time.sleep(10)
	except KeyboardInterrupt:
    		pass	

	# Stop
	self.net.stop()

def main():

    	mm = MininetMan(6633)
	mm.setup_mininet()

if __name__ == "__main__":

	main()

