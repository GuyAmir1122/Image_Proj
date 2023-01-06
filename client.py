from email.mime import image
import socket, pickle
from PIL import Image

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
        to_send.append([x for x in y[start_X, end_X]])
    sock.send(pickle.dumps(to_send))






def main():
    create_pixel_arr()
    sock.connect((IP,PORT))
    while not CONNECTED:
        sock.send("CONNECT###")
    while not FINISH:





if __name__ == "__main__":
    main()