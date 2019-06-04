#全文大部分数字为字符串格式

import requests
import smtplib
from email.mime.text import MIMEText
import time

#配置发信邮箱信息
host = 'smtphz.qiye.163.com'        #需自行查询
user = '14####@stu.hebut.edu.cn' 
password = '########'       #为授权码，不一定与密码相同

#发邮件函数
def send_mail(to_list,subject,content):
    msg=MIMEText(content,'plain','utf-8')    
    msg['subject'] = subject
    msg['from'] = user
    msg['to'] = ','.join(to_list)
    asmtp = smtplib.SMTP()
    asmtp.connect(host,port = '25')
    asmtp.login(user, password)
    asmtp.sendmail(user, to_list, str(msg))
    asmtp.quit()

#定义两个字典,互换n的键值成n1
s = {'G':'正常','Y':'拥挤','R':'满载','S':'维护'}
n = {'1':'艾欧尼亚','2':'比尔吉沃特','14':'黑色玫瑰','4':'诺克萨斯','5':'班德尔城','6':'德玛西亚','7':'皮尔特沃夫','8':'战争学院','9':'弗雷尔卓德','10':'巨神峰','11':'雷瑟守备','12':'无畏先锋','13':'裁决之地','3':'祖安','15':'暗影岛','16':'恕瑞玛','17':'钢铁烈阳','18':'水晶之痕','19':'均衡教派','20':'扭曲丛林','21':'教育网专区','22':'影流','23':'守望之海','24':'征服之海','25':'卡拉曼达','26':'巨龙之巢','27':'皮城警备','30':'男爵领域'}
n1=dict([val,key] for key,val in n.items())

#爬虫函数,最后的r为字典格式例如：{'30': 'G', '21': 'G', '14': 'Y'......}
def get():
    url ='https://apps.game.qq.com/lol/act/a20150325ServerStatus/getServerStatus.php'
    r = requests.get(url)
    r.encoding = 'gbk'
    r = r.text
    r = r[32:-7]
    r = eval(r)
    return r

#按特定格式输出所有大区信息
r = get()
print('---------------------------------------------------------------------------------------------------')
print('各大区服务器状态如下')
print('---------------------------------------------------------------------------------------------------')
j = 1
for i in ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','30']:
    if j%4 == 0:
        print(n[i],s[r[i]])
    else:
        print(n[i],s[r[i]],end='              ')
    j = j + 1
print('---------------------------------------------------------------------------------------------------')

#输入全称，设置用户关注的大区，u为'数字'
print('建议把你常玩的大区设为关注，以定制邮件提醒')
uName = input('请输入你关注的大区名称全称，你亦可退出程序:  ')
while uName not in n1 :
    uName = input('输入错误，请重新输入【大区名称全称】（如：比尔吉沃特、教育网专区、德玛西亚、班德尔城）')
else:
    u = n1[uName]
    print("已成功设置" + uName + "为你的关注")

#初始化，查询用户关注大区状态，发出提醒
sta = s[r[u]]
if sta == '正常' or '拥挤' or '满载':
    i1 = i = 1
else:
    i1 = i = 0

if i == 1:
    print('你关注的大区是：' + sta)
    if sta == '拥挤' or '满载':
        print('但你仍可登陆游戏')
    else:
        print('你可畅玩')                
else:            
    print('你关注的大区正在维护')
    send_mail(['##########@qq.com'],n[u] + '大区正在维护',n[u] + '大区正在维护')
    print('邮件提醒已发送成功')

print('保持程序继续运行，将在大区状态改变时提醒你')

#持续监测是否改变，变动发送邮件
while True :
    time.sleep(300)
    r = get()
    sta = s[r[u]]
    if sta == '正常' or '拥挤' or '满载':
        i1 = 1
    else:
        i1 = 0
    if i1 != i:
        print('你关注的大区状态改变，现在的状态是：' + sta)
        send_mail(['##########@qq.com'],n[u] + '现在的状态是' + sta,n[u] + '现在的状态是' + sta)
        print('邮件提醒已发送成功，保持程序继续运行，将在大区状态再次变化时提醒你')
        i = i1
    else:
        print('你关注的大区状态无变化，现在的状态是：' + sta)
