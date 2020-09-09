#coding:utf8
__author__ = 'yeyong'
import dpkt
import pcap

sniffer = pcap.pcap(name="en0")   #name parameter => interface name
sniffer.setfilter("tcp")                         #filter sentence
cur_timestamp = 0
c=0
caplen = 0
for packet_time,packet_data in sniffer:
    packet_time = int(packet_time)
    if cur_timestamp == packet_time:
        c +=1
        caplen += len(packet_data)
    else:
        print (cur_timestamp, c, caplen)
        cur_timestamp = packet_time
        c=0
        caplen = 0# packet = dpkt.ethernet.Ethernet(packet_data)#二层数据报文嘛# print "SRC IP:%d.%d.%d.%d"%tuple(map(ord,list(packet.data.src)))# print "DST IP:%d.%d.%d.%d"%tuple(map(ord,list(packet.data.dst)))# print "SRC PORT:%s"%packet.data.data.sport# print "DST PORT:%s"%packet.data.data.dport