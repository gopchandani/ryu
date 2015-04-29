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

	print "Setup"

        # Start
        self.net.start()

		
	# Send a packet every 10 second
	print "Ping"
	self.net.pingAll(timeout="10")
	
	print "Stop"

	# Stop
	self.net.stop()

def main():

    	mm = MininetMan(6633)
	mm.setup_mininet()

if __name__ == "__main__":

	main()

