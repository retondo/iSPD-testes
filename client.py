from multiprocessing import Process, Manager, Lock
import socket
import time
import sys

def client(ip, lista, lock):
	HOST = ip
	PORT = 5000
	tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	argc = len(sys.argv)
	t = 0

	print('host:port -> {0}:{1}'.format(HOST, PORT))
	tcp.connect((HOST, PORT))
	print('Para sair use CTRL+X\nProcessando...\n')

	for i in range(int(float(sys.argv[argc-1]))):
		msg ='0.2'
		tcp.send(msg.encode())
                rec = tcp.recv(1024).decode()
                t += float(rec)
        tcp.close()
        l.acquire()
        lista.append(t)
        l.release()

manager = Manager()
l = Lock()
return_time = manager.list()

th1 = Process(target = client, args = ('10.128.0.3', return_time, l, ))
th1.start()
th2 = Process(target = client, args = ('10.128.0.4', return_time, l, ))
th2.start()
th3 = Process(target = client, args = ('10.128.0.8', return_time, l, ))
th3.start()
th4 = Process(target = client, args = ('10.128.0.6', return_time, l, ))
th4.start()

th1.join()
th2.join()
th3.join()
th4.join()

tt = 0
for i in range(4):
        tt += return_time[i]

tt /= 4
print('Resultado final de tempo de execução:', tt)

