## Kiyo

单文件封装的webUI影梭代理工具 For Windows, Linux

### 系统要求

🚦 Windows10 with C++ 2010 plus
🚦 Linux with GLIBC_2.25 plus

### 编译环境

✔ Ubuntu18.04 编译通过
✔ Windows10 19.03 编译通过

### 简介

**Kiyo**通过对socks5协议代理工具库进行封装，可以让你在Windows和Linux系统上无障碍地使用加密的socks5协议进行科学上网，目前没有封装proxy相关库，全局代理需要手动开启，pac模式代理暂时无法实现。

**Kiyo**拥有简单的🌍web主页，开启迅速，只要通过浏览器即可快速配置文件，无需图形化客户端，支持可视化页面下的开启服务和关闭服务，解析ss/ssr订阅链接地址，(暂时只支持Linux系统的后台运行，Windows需要保持命令行的后台开启状态)，二维码导入和批量导入功能将于后续加入。

### 界面

![demo1](http://mgek.cc/store/kiyo/demo1.jpg)

**命令行启动**

![demo2](http://mgek.cc/store/kiyo/demo2.jpg)

### 安装

#### 安装kiyo

<span style="color:#808080">Linux</span>

```bash
$ wget http://hub.lrenj.top/repo/kiyo
```

<span style="color:#808080">Windows</span>

```bash
$ wget http://hub.lrenj.top/repo/kiyo.zip
```

单独运行程序无配置文件

```bash
$ wget http://hub.lrenj.top/repo/kiyo.exe
```

#### 安装ss

仅针对使用ss的情况

```bash
$ pip3 install shadowsocks
```

安装后在终端测试是否安装成功

```bash
$ sslocal
$ ssserver
```

#### 安装自定义代理模式

```bash
Windows Proxifier
Windows版本的代理设置即将加入kiyo
Linux Proxychains
```

### 查看介绍

使用命令`./kiyo info`可以查看**kiyo**的具体信息和使用步骤

### 使用本地代理

#### 🚀开始搭建一个ss代理

基于Windows和Linux的ss代理启动方式略有不同

```bash
$ wget http://hub.lrenj.top/repo/kiyo.zip
$ unzip kiyo && cd kiyo
$ chmod 700 kiyo
$ ./kiyo ss
```

使用`ss`命令开启本地ss代理服务，**kiyo**会主动寻找当前目录下的`local.json`文件作为配置文件启动，如果报Not Found错误需要先创建`local.json`文件

local.json

```json
{
    "server": "server ip",
    "server_port": "8080",
    "local_address": "127.0.0.1",
    "local_port": 2333,
    "password": "password",
    "timeout": 300,
    "method": "rc4-md5",
    "fast_open": false
}
```

默认ss服务启动在本地的`2333`端口，现在打开Windows或者Linux的系统代理设置，在代理地址中填写

| 本地地址  | 监听端口 | 白名单            |
| --------- | -------- | ----------------- |
| 127.0.0.1 | 2333     | 例如www.baidu.com |

使用`-d`参数可以允许ss服务后台运行，即`./kiyo ss -d`，仅支持Linux系统

#### 🚀开始搭建一个ssr代理

**kiyo**对ssr协议代理进行了封装，你无需下载其他库

```bash
$ ./kiyo ssr
```

使用命令`ssr`即可开启ssr本地代理，服务依赖当前目录下的`ssr.json`文件，如果报Not Found错误需要先创建`ssr.json`文件。

你也可以使用`--run`指定配置文件的路径，如：`./kiyo ssr --run /home/ssr/config.json`，注意参数为绝对路径。

ssr.json

```json
{
    "server": "server ip",
    "server_ipv6": false,
    "server_port": 8080,
    "local_address": "127.0.0.1",
    "local_port": 2333,

    "password": "pass",
    "method": "rc4-md5-6",
    "protocol": "auth_aes128_md5",
    "protocol_param": "",
    "obfs": "plain",
    "obfs_param": "",
    "speed_limit_per_con": 0,
    "speed_limit_per_user": 0,

    "additional_ports" : {},
    "timeout": 120,
    "udp_timeout": 60,
    "dns_ipv6": false,
    "connect_verbose_info": 0,
    "redirect": "",
    "fast_open": false,

    "udp_cache": 64
}
```

`method`加密方式
`protocol`协议
`obfs`混淆方式

默认ssr服务启动在本地的`2333`端口，现在打开Windows或者Linux的系统代理设置，在代理地址中填写

| 本地地址  | 监听端口 | 白名单            |
| --------- | -------- | ----------------- |
| 127.0.0.1 | 2333     | 例如www.baidu.com |

对于Linux系统使用`nohup`可以使**kiyo**保持后台运行，即`nohup ./kiyo ssr &`

#### 支持的加密方式

```bash
rc4
rc4-md5
rc4-md5-6

aes-128-ctr
aes-192-ctr
aes-256-ctr

aes-128-cfb
aes-192-cfb
aes-256-cfb

aes-128-cfb8
aes-192-cfb8
aes-256-cfb8

salsa20
chacha20
```

`salsa20,chacha20`需要安装额外的库

#### 支持的协议

```xml
origin
auth_sha1_v4
auth_aes128_md5
auth_aes128_sha1
auth_chain_a
auth_chain_b
```

**如果使用 auth_chain_a 协议，请加密方式选择 none，混淆随意(建议 plain)**

#### 支持的混淆方式

```xml
plain
http_simple
http_post
random_head
tls1.2_ticket_auth
```

默认为`plain`

### 使用webUI

如果你觉得使用命令行过于复杂，可以使用webUI页面，**kiyo**支持在浏览器里修改配置文件

```bash
$ ./kiyo web
```

使用`web`参数开启web服务，默认运行于`5000`端口，此时在浏览器中访问[http://127.0.0.1:5000](http://127.0.0.1:5000)即可进入webUI页面，按下CTRL+C即可退出webUI

![demo1](http://mgek.cc/store/kiyo/demo1.jpg)

额外参数`--port`可以修改webUI运行的端口，如`web --port 8080`
额外参数`--run`可以设置webUI外部访问，如果你在服务器上运行**kiyo**，想要通过外网访问webUI页面，执行`./kiyo web --run`即可通过访问你的服务器ip+端口进入webUI页面。

点击**保存配置**即可保存你在网页上修改的配置参数，未填写的部分将按照默认参数保存
点击**启动服务**即可开启本地代理服务，Linux建议通过命令行
点击**停止服务**即可关闭代理服务
点击**查看全部**可以查看你的配置文件信息

通过`ssr`链接导入暂时不支持

访问地址[http://127.0.0.1:5000/ssr](http://127.0.0.1:5000/ssr)或者点击**ssr设置**即可进入ssr代理服务的设置页面

### 使用服务器模式

✈除了本地代理服务，你还可以使用**kiyo**开启服务器模式，建立一个供外部访问的server(仅支持Linux)

```bash
$ ./kiyo server
```

此服务依赖当前目录下的`server.json`文件

server.json

```json
{
    "server": "0.0.0.0",
    "server_port": "8080",
    "local_address": "127.0.0.1",
    "local_port": 2333,
    "password": "password",
    "timeout": 300,
    "method": "rc4-md5",
    "fast_open": false
}
```

`server_port`代理客户端连接的远程服务器端口
`local_port`本地服务端监听的端口

### 停止

使用命令`./kiyo stop`即可关闭服务(仅支持Linux)
Windows停止请使用webUI里的**停止服务**按钮

### 全部命令

`info` 查看kiyo详细信息
`help` 查看使用帮助
`version` 查看kiyo版本信息
`ss` 启动本地代理服务
`ss -d` 后台运行ss服务
`ssr` 启动本地ssr代理服务
`ssr --run` 指定配置文件路径运行
`server` 启动服务器模式
`stop` 停止服务(linux)
`web` 开启webUI
`web --port` 修改webUI运行端口
`web --run` 开启外网访问
`cd` 彩蛋

### 问题

| 问题                                                   | 错误                           | 解决                                                         |      |
| ------------------------------------------------------ | ------------------------------ | ------------------------------------------------------------ | ---- |
| libpython3.7m.so requires GLIBC_2.25                   | GLIBC_2.25版本低于要求         | 升级系统or放弃治疗                                           | 🔴    |
| cannot connect to 5000或系统不允许一个重复的套接字连接 | 5000端口被占用                 | 关闭占用的程序或修改kiyo运行的端口                           | ✔    |
| Linux上connect to port 5000/2333                       | 无法连接端口可能是防火墙未开启 | 使用`firewall -cmd`命令开放端口                              | ✔    |
| `./kiyo`permission denied                              | 未给足权限                     | chmod 700 kiyo                                               | ✔    |
| local.json not found                                   | 没有配置文件                   | 当前目录新建文件                                             | ✔    |
| no such cmd sslocal/ssserver                           | shadowsocks安装问题            | `pip3 install shadowsocks`若未解决需要为sslocal程序添加软链接 | ✔    |
| webUI运行时终端中的trackback错误                       | web服务错误                    | ctrl+c停止webUI重启web服务                                   | 🔴    |



### 开源许可

📄 **MIT License**

### 版权

® Landers1037

### 依赖的项目

📌 [Shadowsocks](https://github.com/shadowsocks/shadowsocks)
📌 [Click](https://github.com/pallets/click)
📌 [Flask](https://github.com/pallets/flask)