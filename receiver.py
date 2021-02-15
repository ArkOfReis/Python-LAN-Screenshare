from vidstream import StreamingServer
import threading

receiver = StreamingServer('192.168.10.1', 3846)

t = threading.Thread(target=receiver.start_server)
t.start()

while input("") != 'STOP':
	continue

receiver.stop_server()