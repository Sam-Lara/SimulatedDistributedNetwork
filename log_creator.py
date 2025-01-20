import pyshark
import datetime  # for using the timestamp() method -> convert timestamp to seconds

# sources: http://kiminewt.github.io/pyshark/
# (documentation for the pyshark library)

def parse_packets(file):
    # creates packets object that is filtered on udp and tcp protocols 
    packets = pyshark.FileCapture(file, display_filter="udp || tcp")
    # get the time stamp of the first packet to subtract from subsequent packets
    first_packet_timestamp = packets[0].sniff_time
    relative_time = first_packet_timestamp.timestamp()
    # create heading of log file
    with open("logs.txt", "w") as file:
        # format the heading
        file.write(f"{'Type':>10} {'Time(s)':>10} {'Source_IP':>20} {'Destination_IP':>20}")
        file.write(f"{'Source_Port':>20} {'Destination_Port':>20} {'Protocol':>10} {'Length':>10} {'Flags':>10}\n")
        count = 0
        for packet in packets:
            destination_address = packet.ip.dst
            source_address = packet.ip.src
            # set variables to use later
            comm_type = ""
            source_port = ""
            destination_port = ""
            flags = "None"
            length = packet.length
            packet_timestamp = packet.sniff_time
            time_seconds = packet_timestamp.timestamp() - relative_time
            protocol = "None"
            # check whether the packet uses tcp or udp
            if "TCP" in packet:
                source_port = packet.tcp.srcport
                destination_port = packet.tcp.dstport
                flags = packet.tcp.flags
                protocol = "TCP"
                comm_type = "Unicast"

            elif "UDP" in packet:
                source_port = packet.udp.srcport
                destination_port = packet.udp.dstport
                protocol = "UDP"
                comm_type = "Multicast"
            # truncate the float to two decimal places
            time_seconds = f"{time_seconds:.2f}"
            # write to the log file each packet
            file.write(f"{comm_type:>10} {time_seconds:>10} {source_address:>20} {destination_address:>20}")
            file.write(f"{source_port:>20} {destination_port:>20} {protocol:>10} {length:>10} {flags:>10}\n")
            # only write up to 500 packets
            if count == 500:
                break
            count += 1


if __name__ == '__main__':
    file = "./captured_traffic/capture.pcapng"
    parse_packets(file)
    print("done")
