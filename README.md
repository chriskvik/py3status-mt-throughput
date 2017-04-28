## Mikrotik throughput for py3status
Measure interface throughput from your Mikrotik device straight to py3status.

![Image of Yaktocat](http://91.134.217.251/QmgUM.png)

### Requirements
Enable SNMP on your device
```
/snmp set enabled=yes
```

Install dependencies
```
pip3 install pysnmp
```
Copy the script to the appropiate folder.
```
$HOME/.i3/py3status/
```
Get the OID of the interface you want to monitor.

We need the `bytes-in` and `bytes-out` property.
You can print all oid values for your interface by issuing `[admin@MikroTik] > /interface print oid`


Add the module to your i3status.conf
```
order += "mtwan"
mtwan  {
	snmp_host = '192.168.1.1' 
	snmp_port = 161 
	snmp_community = 'public'

	wan_in =  '.1.3.6.1.2.1.31.1.1.1.6.4'  # OID of bytes-in
	wan_out = '.1.3.6.1.2.1.31.1.1.1.10.4' # OID of bytes out
	format = 'bit'                         # Format 'bit' or 'byte'
	acc = 2                                # Set accuracy of calculations (longer poll-time in seconds)
	refresh = 2                            # Sets the time in seconds between each update
        threshold = -1                         # Thresold value for changing to COLOR_HIGH
}
```
All values are listed as default values. Required values are WAN_IN, WAN_OUT and SNMP_HOST.
