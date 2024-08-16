#conda activate weixin
# pip install wxauto 

import os
import sys
import time
from wxauto import WeChat

wx = WeChat()

def saveMsgToFile(chatroom,sender,msg):
    current_path = os.path.dirname(os.path.realpath(__file__))
    dir_path = os.path.join(current_path, f'msgdata\\{time.strftime("%Y%m%d")}')
    if not os.path.isdir(dir_path):
        os.makedirs(dir_path)
        print(f'创建目录：{dir_path}')
    file_path = os.path.join(dir_path, f'{time.strftime("%H")}_{chatroom}.txt')
    with open(file_path, 'a', encoding='utf-8') as f:
        f.write(f'【{sender} 】：\r\n{msg} \r\n\r\n\r\n')


if __name__ == "__main__":
    if len(sys.argv) > 1:
        saveMsgToFile('test','robot',time.strftime("%Y-%m-%d %H:%M:%S"))
        sessions = wx.GetSession()
        for session in sessions:
            print(f"============== 【{session.name}】 ==============")
            print(f"最后一条消息时间: {session.time}")
            print(f"最后一条消息内容: {session.content}")
            print(f"是否有新消息: {session.isnew}")

        msgs = wx.GetAllMessage()
        for msg in msgs:
            print(f'【消息类型】{msg.type} 【发送人】{msg.sender} 【内容】{msg.content} \r\n\r\n\r\n')
    else:
        listen_list = ['经常庆功才能成功']
        #listen_list改为从文件获取内容
        if(os.path.exists('chatroom_list.txt')):
            with open('chatroom_list.txt','r',encoding='utf-8') as fp:
                listen_list = [i.strip() for i in fp.readlines()]


        for i in listen_list:
            try:
                wx.AddListenChat(who=i)
                print(f'开始获取群消息：{i}')
            except Exception as e:
                print(e)


        wait = 10  # 设置10秒查看一次是否有新消息
        while True:
            msgs = wx.GetListenMessage()
            for chat in msgs:
                who = chat.who # 获取聊天窗口名（人或群名）
                one_msgs = msgs.get(chat)   # 获取消息内容
                for msg in one_msgs:
                    print(f'【{time.strftime("%H:%M:%S")}】【来自】{who} 【消息类型】{msg.type} 【发送人】{msg.sender} 【内容】{msg.content} \r\n\r\n')
                    if(msg.type == 'friend' or msg.type == 'self'):
                        saveMsgToFile(who,msg.sender,msg.content)


            time.sleep(wait)