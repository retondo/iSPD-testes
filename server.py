import multiprocessing
import socket
import time

HOST = '10.128.0.8'
PORT = 5000
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)

tcp.bind(orig)
tcp.listen(10)

def calculate(x, range1, range2, out):
        y = 0
        for i in range(range1):
                for i in range(range2):
                        y = y + x
        out.put(y)

while True:
        con, client = tcp.accept()
        print ('Conectado por', client)

        while True:
                msg = con.recv(1024).decode()
                if not msg:     break

                x = float(msg)
                cores = multiprocessing.cpu_count()
                range1 = int(4000 / cores)
                range2 = int(5000 / cores)
                out = multiprocessing.Queue()

                jobs = []
                for i in range(cores):
                        p = multiprocessing.Process(target = calculate, args = (x, range1, range2, out))
                        jobs.append(p)

                temp1 = time.time()

                for i in range(cores):
                        j = jobs[i]
                        j.start()

                for i in range(cores):
                        j = jobs[i]
                        j.join()

                temp2 = time.time() - temp1
                print('Tempo:', temp2)

                ret = str(temp2)
                con.send(ret.encode())
        con.close()

