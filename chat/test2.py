# _*_ coding:utf-8 _*_
# Filename:ClientUI.py
# Python在线聊天客户端

import Tkinter
import tkFont
import socket
import thread
import time
import sys


class ClientUI():
    title = '购物领域客服系统'
    local = '127.0.0.1'
    port = 8808
    global clientSock;
    flag = False

    # 初始化类的相关属性，类似于Java的构造方法
    def __init__(self):
        self.root = Tkinter.Tk()
        self.root.title(self.title)

        # 窗口面板,用4个面板布局
        self.frame = [Tkinter.Frame(), Tkinter.Frame(), Tkinter.Frame(), Tkinter.Frame()]

        # 显示消息Text右边的滚动条
        self.chatTextScrollBar = Tkinter.Scrollbar(self.frame[0])
        self.chatTextScrollBar.pack(side=Tkinter.RIGHT, fill=Tkinter.Y)

        # 显示消息Text，并绑定上面的滚动条
        ft = tkFont.Font(family='Fixdsys', size=11)
        self.chatText = Tkinter.Listbox(self.frame[0], width=70, height=20, font=ft)
        self.chatText['yscrollcommand'] = self.chatTextScrollBar.set
        self.chatText.pack(expand=1, fill=Tkinter.BOTH)
        self.chatTextScrollBar['command'] = self.chatText.yview()
        self.frame[0].pack(expand=1, fill=Tkinter.BOTH)

        # 标签，分开消息显示Text和消息输入Text
        label = Tkinter.Label(self.frame[1], height=2)
        label.pack(fill=Tkinter.BOTH)
        self.frame[1].pack(expand=1, fill=Tkinter.BOTH)

        # 输入消息Text的滚动条
        self.inputTextScrollBar = Tkinter.Scrollbar(self.frame[2])
        self.inputTextScrollBar.pack(side=Tkinter.RIGHT, fill=Tkinter.Y)

        # 输入消息Text，并与滚动条绑定
        ft = tkFont.Font(family='Fixdsys', size=11)
        self.inputText = Tkinter.Text(self.frame[2], width=70, height=3, font=ft)
        self.inputText['yscrollcommand'] = self.inputTextScrollBar.set
        self.inputText.pack(expand=1, fill=Tkinter.BOTH)
        self.inputTextScrollBar['command'] = self.chatText.yview()
        self.frame[2].pack(expand=1, fill=Tkinter.BOTH)

        # 发送消息按钮
        self.sendButton = Tkinter.Button(self.frame[3], text=' 发 送 ', width=10, command=self.sendMessage)
        self.sendButton.pack(expand=1, side=Tkinter.BOTTOM and Tkinter.RIGHT, padx=15, pady=8)

        # 关闭按钮
        self.closeButton = Tkinter.Button(self.frame[3], text=' 关 闭 ', width=10, command=self.close)
        self.closeButton.pack(expand=1, side=Tkinter.RIGHT, padx=15, pady=8)
        self.frame[3].pack(expand=1, fill=Tkinter.BOTH)

        # 接收消息

    def receiveMessage(self):
        try:
            # 建立Socket连接
            self.clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.clientSock.connect((self.local, self.port))
            self.flag = True
        except:
            self.flag = False
            self.chatText.insert(Tkinter.END, '您还未与服务器端建立连接，请检查服务器端是否已经启动')
            return

        self.buffer = 1024
        self.clientSock.send('Y')
        while True:
            try:
                if self.flag == True:
                    # 连接建立，接收服务器端消息
                    self.serverMsg = self.clientSock.recv(self.buffer)
                    if self.serverMsg == 'Y':
                        self.chatText.insert(Tkinter.END, '正在连接，小主稍等一下哦......')
                    # elif self.serverMsg == 'N':
                    #     self.chatText.insert(Tkinter.END, '连接失败，小主您的网络似乎不太好哦......')
                    # elif not self.serverMsg:
                    #     continue
                    # else:
                        time.sleep(1.6)
                        theTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        self.chatText.insert(Tkinter.END, '客服小哎' + theTime + ' 说：\n')
                        self.chatText.insert(Tkinter.END,'您好 ~ 有什么可以为您效劳的呢'.decode('utf-8')+'\n')

                        time.sleep(2.7)
                        theTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        self.chatText.insert(Tkinter.END, '您 ' + theTime + ' 说：\n')
                        self.chatText.insert(Tkinter.END, '我前天刚买的电饭煲，今天就降价了'.decode('utf-8')+'\n')

                        time.sleep(1.3)
                        theTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        self.chatText.insert(Tkinter.END, '客服小哎' + theTime + ' 说：\n')
                        self.chatText.insert(Tkinter.END, '请您输入想要查询的订单号'.decode('utf-8')+'\n')

                        time.sleep(2.4)
                        theTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        self.chatText.insert(Tkinter.END, '您 ' + theTime + ' 说：\n')
                        self.chatText.insert(Tkinter.END, '14975923'.decode('utf-8')+'\n')

                        time.sleep(1.2)
                        theTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        self.chatText.insert(Tkinter.END, '客服小哎' + theTime + ' 说：\n')
                        self.chatText.insert(Tkinter.END,'查询到   订单号 : [ ORDERID _ 14975923 ]   订单金额 : [ 199 ]   下单时间 : [ 20210123 ]  商品 : 苏泊尔电饭煲'.decode('utf-8')+'\n')

                        time.sleep(1.8)
                        theTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        self.chatText.insert(Tkinter.END, '您 ' + theTime + ' 说：\n')
                        self.chatText.insert(Tkinter.END,'对'.decode('utf-8')+'\n')

                        time.sleep(1.2)
                        theTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        self.chatText.insert(Tkinter.END, '客服小哎' + theTime + ' 说：\n')
                        self.chatText.insert(Tkinter.END,'请您提供一下您购买的商品id'.decode('utf-8')+'\n')

                        time.sleep(1.8)
                        theTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        self.chatText.insert(Tkinter.END, '您 ' + theTime + ' 说：\n')
                        self.chatText.insert(Tkinter.END,'001083e72be0672a531b08191a0c9095'.decode('utf-8')+'\n')

                        time.sleep(1.2)
                        theTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        self.chatText.insert(Tkinter.END, '客服小哎' + theTime + ' 说：\n')
                        self.chatText.insert(Tkinter.END,'这边价保10元会在1日内给您返到原账户噢'.decode('utf-8')+'\n')

                        time.sleep(2.1)
                        theTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        self.chatText.insert(Tkinter.END, '您 ' + theTime + ' 说：\n')
                        self.chatText.insert(Tkinter.END,'谢谢'.decode('utf-8')+'\n')

                        time.sleep(0.8)
                        theTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        self.chatText.insert(Tkinter.END, '客服小哎' + theTime + ' 说：\n')
                        self.chatText.insert(Tkinter.END,'不客气的 呢 ~请问还有其他还可以帮到您的吗?'.decode('utf-8')+'\n')
                        time.sleep(5)
                        theTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        # self.chatText.insert(Tkinter.END, '您 ' + theTime + ' 说：\n')
                        self.chatText.insert('quit')


                else:
                    break
            except EOFError, msg:
                raise msg
                self.clientSock.close()
                break

                # 发送消息

    def sendMessage(self):
        # 得到用户在Text中输入的消息
        message = self.inputText.get('1.0', Tkinter.END)
        # 格式化当前的时间
        theTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.chatText.insert(Tkinter.END, '您 ' + theTime + ' 说：\n')
        self.chatText.insert(Tkinter.END, '  ' + message + '\n')
        if self.flag == True:
            # 将消息发送到服务器端
            self.clientSock.send(message.encode('utf-8'));
        else:
            # Socket连接没有建立，提示用户
            self.chatText.insert(Tkinter.END, '您还未与服务器端建立连接，服务器端无法收到您的消息\n')
            # 清空用户在Text中输入的消息
        self.inputText.delete(0.0, message.__len__() - 1.0)

        # 关闭消息窗口并退出

    def close(self):
        sys.exit()

        # 启动线程接收服务器端的消息

    def startNewThread(self):
        # 启动一个新线程来接收服务器端的消息
        # thread.start_new_thread(function,args[,kwargs])函数原型，
        # 其中function参数是将要调用的线程函数，args是传递给线程函数的参数，它必须是个元组类型，而kwargs是可选的参数
        # receiveMessage函数不需要参数，就传一个空元组
        thread.start_new_thread(self.receiveMessage, ())


def main():
    client = ClientUI()
    client.startNewThread()
    client.root.mainloop()


if __name__ == '__main__':
    main()