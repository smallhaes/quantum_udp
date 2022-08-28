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
    #
    time_start = time.time()
    time_flag = False
    try:
        # 记录接收数据数量
        i = 0
        # 等待接收对方发送的数据
        while True:
            recv_data = udp_socket.recvfrom(1024)  # 1024表示本次接收的最大字节数
            i += 1
            time_end = time.time()
            # 第一次收到数据时开始计时
            if time_flag is False:
                print('收到第一条数据，开始计时。。。')
                time_flag = True
                time_start = time.time()
            # 数据传输持续2分钟
            elif time_end - time_start >= 120:
                break

    finally:
        time_cost = time_end - time_start
        per = i / time_cost
        print("{:.2f}秒接收送了{}条数据，平均每秒接收{:.2f}条数据".format(time_cost, i, per))


if __name__ == '__main__':
    print("udp server ")
    main()
