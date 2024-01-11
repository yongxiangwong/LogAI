import psutil
import socket
import platform
import os

#cpu_info = psutil.

#print("CPU型号:%s" % cpu_info.brand)
#print("CPU核心数:%s" % cpu_info.cores)



memory_info = psutil.virtual_memory()

print("内存总量：%s" % memory_info.total)

print("已使用内存：%s" % memory_info.used)

print("内存使用率：%s%%" % memory_info.percent)

# 获取磁盘信息

#disk_info = psutil.disk_info()

#print("磁盘总量：%s" % disk_info.total)

#print("已使用磁盘：%s" % disk_info.used)

#print("磁盘使用率：%s%%" % disk_info.percent)

# 获取网络信息

net_io = psutil.net_io_counters()

print("网络发送字节：%s" % net_io.bytes_sent)

print("网络接收字节：%s" % net_io.bytes_recv)

#print("网络带宽：%.2fMbit/s" % (net_io.bytes_sent + net_io.bytes_recv)/ 1024 / 1024))

# 获取主机名和IP地址

host_name = socket.gethostname()

print("主机名：%s" % host_name)

host_ip = socket.gethostbyname(host_name)

print("IP地址： %s" % host_ip)

# 获取操作系统信息

os_info = platform.platform()

print("操作系统：%s" % os_info)

# 获取Python解释器路径

python_path = os.path.abspath(sys.executable)

print("Python解释器路径：%s" % python_path)