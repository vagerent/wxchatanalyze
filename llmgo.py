'''
发布地址：https://pypi.org/project/volcengine-python-sdk
源码地址：https://github.com/volcengine/volcengine-python-sdk/tree/master/volcenginesdkarkruntime
pip install 'volcengine-python-sdk[ark]'
python setup.py install --user
示例代码：https://www.volcengine.com/docs/82379/1302008
pip install --user volcengine
pip install --upgrade volcengine
'''


import os
import time
from volcenginesdkarkruntime import Ark

#下面跟画图相关
from volcengine.visual.VisualService import VisualService

apikey="换成你的豆包apikey，从后面链接获取-xxxx-xxxx-xxxx-xxxxxxxxxx" #https://console.volcengine.com/ark/region:ark+cn-beijing/apiKey?apikey=%7B%7D
client = Ark(api_key=apikey,
    base_url="https://ark.cn-beijing.volces.com/api/v3", #域名部分可查看https://www.volcengine.com/docs/82379/1302013
    timeout=120,
    max_retries=2,
)



def chatFileProcess(datestr):
    newlist=[]

    # 如果datestr为空
    if datestr == "":
        datestr=time.strftime("%Y%m%d")
    # 如果datestr不是数字
    if not datestr.isdigit():
        return newlist
    current_path = os.path.dirname(os.path.realpath(__file__))
    dir_path = os.path.join(current_path, f'msgdata\\{datestr}')
    if not os.path.isdir(dir_path):
        return newlist
    #列出目录中所有文件，并按照文件创建时间排序
    files_and_dirs = os.scandir(dir_path)
    
    # 使用 sorted() 函数对文件和子目录按照创建时间倒序排序
    sorted_files_and_dirs = sorted(files_and_dirs, key=lambda entry: entry.stat().st_ctime_ns) #, reverse=True

    #循环他
    for file in sorted_files_and_dirs:
        if file.name.endswith('.txt'):
            file_path = os.path.join(dir_path, file.name)
            # file.name提取_和.中间部分名称
            newfile_name = file.name.split('_')[1].split('.')[0]
            newfile_name2 = f'{datestr}_{newfile_name}.txt'
            if newfile_name2 not in newlist:
                newlist.append(newfile_name2)
            #把文件内容追加到一个新文件中
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                with open(os.path.join(current_path, f'msgdata\\{datestr}_{newfile_name}.txt'), 'a', encoding='utf-8') as fa:
                    fa.write(content)
                
    return newlist


def analyzeChatData_QA(context):
    completion = client.chat.completions.create(
        model="ep-XXXXXXXXXXXXXXX-XXXX", #模型接入点：https://console.volcengine.com/ark/region:ark+cn-beijing/endpoint?config=%7B%7D 火山方舟-在线推理-创建推理接入点
        messages = [
            {"role": "user", "content": f"我会给你提供微信群里的聊天记录，请根据该聊天记录的内容，总结群里提出的问题以及讨论出的相应的解决方案。聊天记录如下：\r\n\r\n\r\n{context}"},
        ],
    )
    return completion.choices[0].message.content

def analyzeChatData_Joke(context):
    completion = client.chat.completions.create(
        model="ep-XXXXXXXXXXXXXXX-XXXX", #模型接入点：https://console.volcengine.com/ark/region:ark+cn-beijing/endpoint?config=%7B%7D 火山方舟-在线推理-创建推理接入点
        messages = [
            {"role": "user", "content": f"你是一个敏锐的心理分析师，能够通过聊天内容的蛛丝马迹分析人物的性格。我会给你提供微信群里的聊天记录，请根据该聊天记录的内容，用黑色幽默的评语总结群里每个人的性格。聊天记录如下：\r\n\r\n\r\n{context}"},
        ],
    )
    return completion.choices[0].message.content


def analyzeChatData_MBTI(context):
    completion = client.chat.completions.create(
        model="ep-XXXXXXXXXXXXXXX-XXXX", #模型接入点：https://console.volcengine.com/ark/region:ark+cn-beijing/endpoint?config=%7B%7D 火山方舟-在线推理-创建推理接入点
        messages = [
            {"role": "user", "content": f"你是一个敏锐的心理分析师，能够通过聊天内容的蛛丝马迹分析人物的性格。我会给你提供微信群里的聊天记录，请根据该聊天记录的内容，总结群里每个人的MBTI性格，并分析。聊天记录如下：\r\n\r\n\r\n{context}"},
        ],
    )
    return completion.choices[0].message.content


def analyzeChatData_Love(context):
    completion = client.chat.completions.create(
        model="ep-XXXXXXXXXXXXXXX-XXXX", #模型接入点：https://console.volcengine.com/ark/region:ark+cn-beijing/endpoint?config=%7B%7D 火山方舟-在线推理-创建推理接入点
        messages = [
            {"role": "user", "content": f"你是一个敏感的心理分析师，能够通过聊天内容的蛛丝马迹分析人物的性格和爱情。我会给你提供微信群里的聊天记录，请仔细阅读这些聊天记录的内容，分析群里谁喜欢谁或者对其有好感。聊天记录如下：\r\n\r\n\r\n{context}"},
        ],
    )
    return completion.choices[0].message.content


current_path = os.path.dirname(os.path.realpath(__file__))
newlist=chatFileProcess('')
if newlist:
    for file in newlist:
        filefullpath=os.path.join(current_path, f'msgdata\\{file}')
        with open(filefullpath, 'r', encoding='utf-8') as f:
            content = f.read()
            sss1=analyzeChatData_QA(content)
            print(f'{sss1}============================================================================\r\n\r\n\r\n\r\n')
            sss2=analyzeChatData_Joke(content)
            print(f'{sss2}============================================================================\r\n\r\n\r\n\r\n')
            sss3=analyzeChatData_MBTI(content)
            print(f'{sss3}============================================================================\r\n\r\n\r\n\r\n')
            sss4=analyzeChatData_Love(content)
            print(f'{sss4}============================================================================\r\n\r\n\r\n\r\n')