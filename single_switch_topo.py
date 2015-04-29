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

	h1 = self.net.getNodeByName("h1")
	h2 = self.net.getNodeByName("h2")
	
	# Disable ICMP reply packets on host-2 so only a single packet is sent from h1->h2 and no replies
	h2.cmd('echo "1" >  /proc/sys/net/ipv4/icmp_echo_ignore_all')
		
	# Start at h1  ping every 10 seconds
	h1.cmd('ping -i 10 10.0.0.2')

	# Stop
	self.net.stop()

def main():

    	mm = MininetMan(6633)
	mm.setup_mininet()

if __name__ == "__main__":

	main()

