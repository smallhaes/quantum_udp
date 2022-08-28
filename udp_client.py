import socket
import random
import time
from list_content import list_content


def generate_content():
    # 每句话的长度
    len_sentence = random.randint(2, 51)
    # 拼凑句子
    sen = ""
    for i in range(1, len_sentence):
        sen += random.choice(list_content)
    return sen


def main():
    # udp 通信地址，IP+端口号
    # udp_addr = ('127.0.0.1', 9999)
    # 业务B的IP
    udp_addr = ('20.1.1.2', 7790)
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        # 记录发送的数据量
        i = 0
        # 记录发送时间
        time_start = time.time()
        # 无限制发送
        while True:
            sen = generate_content()
            udp_socket.sendto(sen.encode('utf-8'), udp_addr)
            i += 1
    finally:
        time_end = time.time()
        time_cost = time_end - time_start
        per = i / time_cost
        print("{:.2f}秒发送了{}条数据，平均每秒发送{:.2f}条数据".format(time_cost, i, per))
        # 5. 关闭套接字
        udp_socket.close()


if __name__ == '__main__':
    print("udp client ")
    main()
