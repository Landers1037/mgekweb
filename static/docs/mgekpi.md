# Mgekpi
整合版命令行下载工具，整合aria2，you-get,wget

### 下载

```shell
$ git clone https://github.com/Landers1037/Mgekpi.git
```

### 使用

```shell
cd linux-ver
$ sudo chmod +x mgekpi.py
$ ./mgekpi.py
#####或者#####
cd linux-ver
$ sudo chmod +x mgekpi
$ ./mgekpi
```

#### windows系统

```shell
cd win-ver
$ python mgekpi.py
#####或者#####
$ mgekpi.exe
```

### 命令

```shell
>-h
|使用帮助 输入-h查看全部命令
        |mgekpi 支持aria2,you-get,curl模式
        |输入aria  进入aria2单任务下载模式,添加链接任务|
        |输入aria2 进入aria2后台服务模式,aria2运行于后台,后台多任务下载，输入show查看任务
        |输入get   进入you-get下载模式,支持下载音乐，视频，短视频资源
        |输入exit  退出下载模式，进入主界面
        |输入kill  退出所有的aria2下载任务，关闭aria2服务，退出程序
```

```shell
>aria
    进入aria2命令行下载模式(单任务下载)
    & mgek|A
```

输入aria即可进入使用aria2进行单任务下载

单任务模式下，输入-c打开配置

```shell
& mgek|A -c
        1.dht监听端口
        2.bt监听端口
        3.最大线程数
        4.允许线程数
        5.同时下载文件数
        6.是否断点续传
        7.最大下载速率(0为不限制)
        8.后台保护进程

        输入序号修改
```

```shell
>aria2
    进入aria2服务下载模式(后台)
    aria2
```

输入aria2即可进入使用aria2后台服务下载多任务

后台服务模式下，输入-s或show，查看下载任务

```shell
aria2 show
没有进行的任务
```

```shell
>get
    进入you-get下载模式
    & mgek|G
```

输入get使用you-get下载文件

```shell
& mgek|G -o E:\download url
```

使用-o选择下载路径

```shell
& exit
```

输入exit退出下载模式

```shell
>kill
    关闭所有aria2c进程
    >>>>>>>>>>>>>>>>>>>>关闭完成
    感谢使用
```

输入kill关闭后台aria2服务，退出程序