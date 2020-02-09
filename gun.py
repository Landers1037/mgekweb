# 并行工作进程数
workers = 1
# 指定每个工作者的线程数
threads = 8
# 监听内网端口80
bind = '0.0.0.0:1317'
# 设置最大并发量
worker_class = "gevent"
worker_connections = 500
timeout = 600
reload=True
