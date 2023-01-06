import socket
import threading

IP = "0.0.0.0"
PORT = 6969
CLIENTS = 0
ACCEPTING = True
FLASHLIGHT = 50
CLIENT_DICT = {1:None,2:None,3:None,4:None}
PHOTOSIZE = 400
MIDDLE = PHOTOSIZE//2

def get_av():
    for key in CLIENT_DICT:
        if CLIENT_DICT[key] != None:
            return key
    return -1

def check_quarter(x,y,quarter):
    if quarter == 1:
        if x<MIDDLE and y<MIDDLE:
            return True
        return False
    
    if quarter == 2:
        if x>MIDDLE-FLASHLIGHT and y<MIDDLE:
            return True
        return False
    
    if quarter == 3:
        if x<MIDDLE and y>MIDDLE-FLASHLIGHT:
            return True
        return False
    
    if quarter == 4:
        if x>MIDDLE-FLASHLIGHT and y>MIDDLE-FLASHLIGHT:
            return True
        return False
    

def get_pixels_by_quarter(x,y,quarter):
    #[xstart,xend,ystart,yend]
    values = [0,0,0,0]
    if quarter == 1:
        values[0] = x
        values[1] = min(x+FLASHLIGHT,MIDDLE)
        values[2] = y
        values[3] = min(y+FLASHLIGHT,MIDDLE)
    
    elif quarter == 2:
        values[0] = max(x,MIDDLE)-MIDDLE
        values[1] = x+FLASHLIGHT-MIDDLE
        values[2] = y
        values[3] = min(y+FLASHLIGHT,MIDDLE)   
    
    elif quarter == 3:
        values[0] = x
        values[1] = min(x+FLASHLIGHT,MIDDLE)
        values[2] = max(MIDDLE,y)-MIDDLE
        values[3] = y+FLASHLIGHT-MIDDLE
    
    else:
        values[0] = max(x,MIDDLE)-MIDDLE
        values[1] = x+FLASHLIGHT-MIDDLE
        values[2] = max(MIDDLE,y)-MIDDLE
        values[3] = y+FLASHLIGHT-MIDDLE

    return values
    




def get_pixels(x,y):
    diction = {}
    for i in range(1,5):
        if check_quarter(x,y,i):
            diction[i] = get_pixels_by_quarter(x,y,i)
    return diction


def handle_client(cli_sock,quarter):
    pass



def main():
    threads = []
    srv_sock = socket.socket()
    srv_sock.bind((IP,PORT))
    srv_sock.listen(5)
    while ACCEPTING:
        quarter = get_av()
        if quarter == -1:
            continue

        cli_sock,addr = srv_sock.accept()
        t = threading.Thread(target=handle_client,args=(cli_sock,quarter))
        t.start()


if __name__ == "__main__":
    main()