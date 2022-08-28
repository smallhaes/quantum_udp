import socket
import time

def main():
    # udp 通信地址，IP+端口号
    # udp_addr = ('127.0.0.1', 9999)
    # 业务A的ip
    udp_addr = ('30.1.1.2', 6690)
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定端口
    udp_socket.bind(udp_addr)

    try:
        # 记录接收数据数量
        i = 0
        # 记录时间
        time_start = time.time()
        # 等待接收对方发送的数据
        while True:
            recv_data = udp_socket.recvfrom(1024)  # 1024表示本次接收的最大字节数
            i += 1
            # 打印接收到的数据
            # print("[From %s:%d]:%s" % (recv_data[1][0], recv_data[1][1], recv_data[0].decode("utf-8")))
    finally:
        time_end = time.time()
        time_cost = time_end - time_start
        per = i / time_cost
        print("{:.2f}秒接收送了{}条数据，平均每秒接收{:.2f}条数据".format(time_cost, i, per))


if __name__ == '__main__':
    print("udp server ")
    main()
