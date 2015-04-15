sudo ovs-vsctl -- set Port s1-eth1 qos=@newqos -- --id=@newqos create QoS type=linux-htb other-config:max-rate=1000000000 queues=1=@q1 -- --id=@q1 create Queue other-config:min-rate=3000000 other-config:max-rate=3000000
sudo ovs-vsctl -- set Port s1-eth1 qos=@newqos -- --id=@newqos create QoS type=linux-htb other-config:max-rate=1000000000 queues=2=@q2 -- --id=@q2 create Queue other-config:min-rate=4000000 other-config:max-rate=4000000

sudo ovs-vsctl -- set Port s1-eth2 qos=@newqos -- --id=@newqos create QoS type=linux-htb other-config:max-rate=1000000000 queues=1=@q1 -- --id=@q1 create Queue other-config:min-rate=3000000 other-config:max-rate=3000000
sudo ovs-vsctl -- set Port s1-eth2 qos=@newqos -- --id=@newqos create QoS type=linux-htb other-config:max-rate=1000000000 queues=2=@q2 -- --id=@q2 create Queue other-config:min-rate=4000000 other-config:max-rate=4000000

sudo ovs-vsctl -- set Port s1-eth3 qos=@newqos -- --id=@newqos create QoS type=linux-htb other-config:max-rate=1000000000 queues=1=@q1 -- --id=@q1 create Queue other-config:min-rate=3000000 other-config:max-rate=3000000
sudo ovs-vsctl -- set Port s1-eth3 qos=@newqos -- --id=@newqos create QoS type=linux-htb other-config:max-rate=1000000000 queues=2=@q2 -- --id=@q2 create Queue other-config:min-rate=4000000 other-config:max-rate=4000000
