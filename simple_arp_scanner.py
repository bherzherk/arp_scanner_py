#!/usr/bin/env python3

import scapy.all as scapy 
import argparse

def get_arguments():
    parser = argparse.ArgumentParser(description="Simple ARP scanner")
    parser.add_argument("-t", "--target", required=True, dest="target", help="Host / IP to scan")

    args = parser.parse_args()

    return args.target

def scan(ip):
    scapy.arping(ip)

def run_scanner():
    target = get_arguments()
    scan(target)

if __name__ == "__main__":
    run_scanner()
