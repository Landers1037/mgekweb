# mgekssr
docker打包的快速部署flask可视化ssr链接爬虫

### 使用

#### 拉取镜像

```sh
docker pull landers1037/mgekflask
```

#### 运行

```sh
docker run -itd -p 5000:80 mgekflask
```

访问本地的[5000](http://127.0.0.1:5000)端口

### 依赖

docker镜像基于python3.7官方docker镜像

本Flask项目基于Flask1.0.3

#### Dockerfile

```
FROM python:3.7
MAINTAINER landers liaorenj@gmail.com
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt
EXPOSE 80
RUN chmod +x /app/start.sh
ENTRYPOINT /app/start.sh
```

#### requirements.txt

```
gunicorn
flask
pyquery
requests
schedule
```

### 实现

所有数据均保存为json文件，实现无数据库模式

爬虫效率：每6小时爬取一次

### 示例图

![demo](http://file.mgek.cc/images/mgek/mgekssr/demo.png)