# simple-email-sms
一个简单的python实现的邮件服务，短信服务

also provide a sms.service to notice you about your server status

[中文文档](https://github.com/Landers1037/simple-email-sms/blob/master/README-CN.md)

### 😁Demand

python3.7 ,twilio ,shcedule ,twilio token,psutil

### ⚙Install

```shell
git clone https://github.com/Landers1037/simple-email-sms.git
```

or you can use one step shell `start.sh`

```shell
./start.sh
```



```python
pip install schedule
pip install twilio
pip install psutil
```

get a Twilio account at  [Twilio](https://www.twilio.com/try-twilio)

------

use service.json to add your infomation

```json
{
    "mail": "true",
    "sms": "true",
    "notice": "true",
    "username": "xxx@163.com",
    "password": "123456",
    "sender": "xxx@163.com",
    "receiver": ["xxx@qq.com"],
    "subject": "python mail test",
    "source": "xxx@163.com <xxx@163.com>",
    "text": "just a email test,please ignore",
    "smtp": "smtp.163.com",
    "ssl": "false",
    "port": 25,
    "mailtime": "06:30",
    "account_sid": "ACc986e47ssxxxxxxx",
    "auth_token": "d42852c86aae943e76",
    "from_phone": "+1555555",
    "to_phone": "+8610086",
    "message": "this is a sms test send from xxx",
    "smstime": "18:30",
    "sysprocess": ["nginx", "python", "aria2c"]

}
```

`mail service use smtp.163.com as default`

### 📝Instructions

`mail` is true,the mail.service is active

`sms` is true,the sms.service is active

`notice` is true,send linux server spy log by sms

`username` is your mail account

`password` is your mail passwd

`sender` is the same as username

`receiver` is the receive mailbox,it's a list

`subject` is the mail theme

`source` is the mail source,same as username

`text` is the text you want to mail

`smtp` is the default smtp address

`ssl` is true,mail will use smtp_ssl,then port must be 465

`port` for smtp use 25,for ssl use 465

`mailtime` is the time your want to set for mail

`account_sid` is your twilio accound_sid

`auth_token` is your twilio token

`from_phone` is your twilio phone number

`to_phone` is your own phone number 

`message` is the message you want to send by sms

`smstime` is the time you want to set for sms

`sysprocess` is the list of system process you want to spy

### 🔴Log output

once you have active or inactive your service,the log will be saved in `log.json`

once an error happend,it will be saved in `log.json`

### 🤪Start

```bash
$ python3 /home/pyservice/simple-email-sms/service.py
```

to run in background

```bash
$ nohup python3 /home/pyservice/simple-email-sms/service.py &
```

see log

```bash
$ cat ~/simple-email-sms/log.json
```

send server process log by sms

```json
"notice": "true",
"sysprocess": ["nginx", "python", "aria2c"]
```

add process you want to `sysprocess`

once `notice` is true,sms.service will send system log like the following,`message` will be inactive and not be send

```nginx
Sent from your Twilio trial account
内存占用率：37.6%
vsftpd:ok
aria2c:ok
nginx:ok
```