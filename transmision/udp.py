import socket
import rospy

ip = '192.168.244.161'
port = 9119
password = 'ITS'

def send(pesan):
    print('dah jalan nih')
    kirim = password + pesan
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(kirim.encode(), (ip, port))
    sock.close()

def receive():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((ip, port))

    while True:
        data, address = sock.recvfrom(4096)
        pesan = data.decode()
        cek = pesan[:3]
        if cek == password:
            isi = pesan[3:]
            print(f'Pesan masuk: {isi}')
        else:
            print('Password salah cuk')

def truster_belakang_kanan():
    return 157
    
def truster_belakang_kiri():
    return 157
    
def servo_kanan():
    return 157
    
def servo_kiri():
    return 157

def servo_waterpump():
    return 157
    
def waterpump():
    return 157

if __name__ == '__main__':
    rospy.init_node('Transmision')
    rospy.loginfo('Ready')
    
    send(truster_belakang_kanan())
    send(truster_belakang_kiri())
    send(servo_kanan())
    send(servo_kiri())
    send(servo_waterpump())
    send(waterpump())
    
    receive()
    rospy.spin()
