from multiprocessing import Process, Manager, Lock
import socket
import time
import sys

manager = Manager()
l = Lock()
return_time = manager.list()
servers = 4
arg = sys.argv[len(sys.argv)-1]

def client(ip, lista, lock, a):
	HOST = ip
	PORT = 5000
	tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	t = 0

	print('host:port -> {0}:{1}'.format(HOST, PORT))
	tcp.connect((HOST, PORT))
	print('Para sair use CTRL+X\nProcessando...\n')

	for i in range(int(float(a)/servers)):
		msg ='0.2'
		tcp.send(msg.encode())
		rec = tcp.recv(1024).decode()
		t += float(rec)
	tcp.close()
	l.acquire()
	lista.append(t)
	l.release()

p1 = Process(target = client, args = ('104.197.245.227', return_time, l, arg, ))
p2 = Process(target = client, args = ('104.154.28.83', return_time, l, arg, ))
p3 = Process(target = client, args = ('104.155.136.135', return_time, l, arg, ))
p4 = Process(target = client, args = ('104.198.25.74', return_time, l, arg, ))

p1.start()
p2.start()
p3.start()
p4.start()

p1.join()
p2.join()
p3.join()
p4.join()

tt = 0
for i in range(servers):
        tt += return_time[i]

tt /= servers

# Escreve no arquivo (cria se não existir) o tempo total
fn = str(arg)+".txt"
f = open(fn, "a")
f.write(str(tt)+"\n")
f.close()

print('Resultado final de tempo de execução:', tt)

