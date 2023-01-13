import socket, pickle
from PIL import Image
import tcp_by_size

#




sock = socket.socket()
IP = ""
PORT = 6969
PIXELS = []
PHOTO_PATH = ""
FINISH = False
CONNECTED = False

def create_pixel_arr():
    im = Image.open(PHOTO_PATH)
    all_pixels = im.load() #100*100 pixels
    PIXELS = [all_pixels[i:i+100] for i in range(0,100*100,100)]



def send_wanted_pixels(start_X, end_X, start_Y, end_Y):
    to_send = []
    for y in range(start_Y, end_Y):
        to_send.append([x for x in PIXELS[y][start_X, end_X]])
    tcp_by_size.send_with_size(sock, pickle.dumps(to_send))


def recv_wanted_pixels():
    data = tcp_by_size.recv_with_size(sock)
    coardinates = pickle.loads(data)
    return coardinates



def main():
    create_pixel_arr()
    sock.connect((IP,PORT))
    """    while not CONNECTED:
        tcp_by_size.send_with_size("CONNECT")
        data = tcp_by_size.recv_by_size(sock)
        if data == "CONNECTED":
            CONNECTED = True"""
    while not FINISH:
        coardinates = recv_wanted_pixels()
        send_wanted_pixels(coardinates[0], coardinates[1], coardinates[2], coardinates[3])





if __name__ == "__main__":
    main()