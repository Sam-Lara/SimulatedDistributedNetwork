#!/bin/bash
# source: https://www.wireshark.org/docs/man-pages/dumpcap.html
# create a variable that is set to the bridge interface -> represents Proj1-distributed-network
interface=$(ifconfig -a | grep -o 'br-[a-zA-Z0-9]*')
# use dumpcap to write traffic to a file using the desired interface
dumpcap -i $interface -w /captured_traffic/capture.pcapng
