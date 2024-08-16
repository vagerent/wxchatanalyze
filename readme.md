## How can it work?

### 1. Automatically records WeChat group chats or private conversation logs with someone, and saves them to the `msgdata/Date` directory every hour.
### 2. Invokes the DouBao large model to analyze these chat contents.

## Current Analysis Scenarios

### 1. Summarizes the issues raised in the group and the corresponding solutions discussed.
### 2. Analyzes each person's personality through the lens of dark humor and sharp-tongued tags.
### 3. Analyzes each person's MBTI personality type.
### 4. Determines whether they love me and how I should proceed subsequently.
### 5. Analyzes the true relationship between the chat participants.

![screenshot](screenshot.png){: width="50%"}

## How to Download

```bash
git clone URL_ADDRESS
```

## Install Dependencies

```bash
pip install wxauto
pip install 'volcengine-python-sdk[ark]'
pip install volcengine
```

## How to Use

1. Set up the `chatroom_list.txt` file, listing the names of the chat windows, one per line.
2. Open the WeChat PC client, then open the group or private chat window.
3. Execute `python mywxhelper.py` to begin recording chat logs.
4. Collect a day's worth of chat content, then execute `python llmgo.py` to start analyzing the chat logs.
5. Remember to update the DouBao API key and model in `llmgo` first.

## Contact Me:

vagerent@126.com
```
