import socket
import struct
from threading import Thread
from time import sleep, time

from numpy import array, linspace

import quad

UDP_PORT = 5005
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('', UDP_PORT))

v = array([0, 0])


def udp_server():
    global v
    while True:
        message, address = server_socket.recvfrom(1024)
        v = struct.unpack('ff', message)
        v = array(v)*0.01


udp_thread = Thread(target=udp_server)
udp_thread.start()
while True:
    t = time()
    positions = quad.walk_positions(v, t)
    servo_angles = quad.pos_to_angles(positions)
    quad.set_servos(servo_angles)
    sleep(0.05)
