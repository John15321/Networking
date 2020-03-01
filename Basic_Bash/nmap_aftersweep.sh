#!/bin/bash
for ip in $(cat iplist.txt); do nmap -p 80 -T4 $ip & done # scans for open ip ports