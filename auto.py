#!/usr/bin/python3
# -*- coding:utf-8 -*-
from wxpy import *
import os
import time
import datetime
import re


if os.path.exists('itchat.pkl'):
	tn = time.time()
	ft = os.path.getctime('itchat.pkl')
	if(tn - ft -900) > 0:
		os.remove('itchat.pkl')

bot = Bot(console_qr=True,cache_path='/root/itchat/itchat.pkl')
#自动消除手机端的新消息小红点提醒

bot.auto_mark_as_read = True
zhou = bot.friends().search('周杨洋')[0]
weng = bot.friends().search('Miss')[0]
@bot.register([zhou,weng],TEXT)
def auto_reply(msg):
    if "S" == msg.text:
        #print ("程序启动")
        if os.path.exists('/root/itchat/text.txt'):
            os.remove('/root/itchat/text.txt')
            #print ('text.txt删除完成！')
        else:
            return ('初始化完成！')
        return ("程序启动，请发送数据！")
        
    if "良月教育" in msg.text:
        msg_text = msg.text
        print (msg_text)
        msg_re = re.findall(r'\d+月\d+\S*工作\S+',msg_text)
        msg_process = msg_text[(msg_text.index(msg_re[0]) + len(msg_re[0])): (msg_text.index(msg_re[1]) - 1)]
        print (msg_process)
        a = msg_process.split("\n")
        while "" in a:
            a.remove('')
        for i in range(len(a)):
            result_F = (a[i][(a[i].index('.') + 1):])
            #print (result_F)
            with open('/root/itchat/text.txt',"a") as fw:
                fw.write(result_F)
                fw.write('\n')
        print ("请发送下一条数据，或者发送' E '完成！")
        return ("请发送下一条数据，或者发送' E '完成！")
        
    if "E" == msg.text:
        #print ("开始处理数据")
        if not os.path.exists('/root/itchat/text.txt'):
            return ('数据不存在请重新输入')
        if os.path.exists('/root/itchat/text_new.txt'):
            os.remove('/root/itchat/text_new.txt')
        with open('/root/itchat/text.txt',"r") as fr:
            result = fr.read()
        a = result.split("\n")
        while "" in a:
            a.remove('')
        for i in range(len(a)):
            result_F = (str(i + 1) + '.' + a[i])
            with open('/root/itchat/text_new.txt',"a") as fw:
                result_F = result_F.strip().strip("。").strip("，").strip(",").strip("；")
                result_F = result_F + "。"
                fw.write(result_F)
                fw.write('\n')
        with open ('/root/itchat/text_new.txt',"r") as fr:
            result_new = fr.read()
        t_day = datetime.datetime.now().strftime('%m月%d日')
        print ('【广电新艺堂.良月教育】\n【市场部{0}工作总结】\n'.format(t_day) + result_new )
        return ('【广电新艺堂.良月教育】\n【市场部{0}工作总结】\n'.format(t_day) + result_new )

embed(banner='hi 现在开始快乐之旅！')
