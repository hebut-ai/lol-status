import requests
import smtplib
from email.mime.text import MIMEText

host = 'smtphz.qiye.163.com'
user = '14####@stu.hebut.edu.cn' 
password = '###########'
 
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

s = {'G':'正常','Y':'拥挤','R':'满载','S':'维护'}
n = {'1':'艾欧尼亚','2':'比尔吉沃特','14':'黑色玫瑰','4':'诺克萨斯','5':'班德尔城','6':'德玛西亚','7':'皮尔特沃夫','8':'战争学院','9':'弗雷尔卓德','10':'巨神峰','11':'雷瑟守备','12':'无畏先锋','13':'裁决之地','3':'祖安','15':'暗影岛','16':'恕瑞玛','17':'钢铁烈阳','18':'水晶之痕','19':'均衡教派','20':'扭曲丛林','21':'教育网专区','22':'影流','23':'守望之海','24':'征服之海','25':'卡拉曼达','26':'巨龙之巢','27':'皮城警备','30':'男爵领域'}

url ='https://apps.game.qq.com/lol/act/a20150325ServerStatus/getServerStatus.php'
r = requests.get(url)
r.encoding = 'gbk'
r = r.text
r = r[32:-7]
r = eval(r)

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
if s[r['2']] != '正常':
    print('注意：我关注的比尔吉沃特大区不正常，现在的状态是：' + s[r['2']])
    #send_mail(['1079919699@qq.com'],'比尔吉沃特状态异常提醒',s[r['2']])
    print('邮件提醒已发送成功')