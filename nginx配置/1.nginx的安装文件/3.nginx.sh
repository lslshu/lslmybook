#！bin/bash
#主菜单
menu()
{
	clear
	cat <<EOF
	   #这是一个菜单
	   1.安装nginx
	   2.卸载nginx
	   3.退出脚本
EOF
read -p "请输入数字[1-3]:" list
case $list in
	1)
		nginx_install
	;;
	2)
        nginx_uninstall
    ;;
    3)
        echo "退出中..."
        sleep 2
        exit 0
    ;;
esac
}
#安装nginx
nginx_install()
{
	cat <<EOF
	###########################
	Nginx安装版本
	1.安装12
	2.安装14
	3.安装16
	4.安装17
EOF
read -p "请输入数字[1-4]：" ver
if [[ "$ver" -eq 1 ]]
 then
	wget http://nginx.org/download/nginx-1.12.2.tar.gz
	tar -zxvf nginx-1.12.2.tar.gz
    cd nginx-1.12.2 
elif [[ "$ver" -eq 2 ]]
 then
	wget http://nginx.org/download/nginx-1.14.2.tar.gz
	tar -zxvf nginx-1.14.2.tar.gz
    cd nginx-1.14.2 
elif [[ "$ver" -eq 3 ]]
 then
	wget http://nginx.org/download/nginx-1.16.1.tar.gz
		tar -zxvf nginx-1.16.1.tar.gz
    cd nginx-1.16.1 
elif [[ "$ver" -eq 4 ]]
 then
	wget http://nginx.org/download/nginx-1.17.10.tar.gz
	tar -zxvf nginx-1.17.10.tar.gz
    cd nginx-1.17.10
else
	echo "没有相应的版本，请重新运行脚本"
	sleep 2
	exit 2
fi
yum install gcc gcc-c++ pcre pcre-devel zlib zlib-devel openssl openssl-devel -y
groupadd www
useradd -g www www
./configure --prefix=/usr/local/nginx --without-http_memcached_module --user=www --group=www --with-http_stub_status_module --with-http_ssl_module --with-http_gzip_static_module
make && make install 
/usr/local/nginx/sbin/nginx
echo '#!/bin/bash
# chkconfig: - 30 21
# description: http service.
# Source Function Library
. /etc/init.d/functions
# Nginx Settings
NGINX_SBIN="/usr/local/nginx/sbin/nginx"
NGINX_CONF="/usr/local/nginx/conf/nginx.conf"
NGINX_PID="/usr/local/nginx/logs/nginx.pid"
RETVAL=0
prog="Nginx"
start() {
echo -n $"Starting $prog: "
mkdir -p /dev/shm/nginx_temp
daemon $NGINX_SBIN -c $NGINX_CONF
RETVAL=$?
echo
return $RETVAL
}
stop() {
echo -n $"Stopping $prog: "
killproc -p $NGINX_PID $NGINX_SBIN -TERM
rm -rf /dev/shm/nginx_temp
RETVAL=$?
echo
return $RETVAL
}
reload(){
echo -n $"Reloading $prog: "
killproc -p $NGINX_PID $NGINX_SBIN -HUP
RETVAL=$?
echo
return $RETVAL
}
restart(){
stop
start
}
configtest(){
$NGINX_SBIN -c $NGINX_CONF -t
return 0
}
case "$1" in
start)
start
;;
stop)
stop
;;
reload)
reload
;;
restart)
restart
;;
configtest)
configtest
;;
*)
echo $"Usage: $0 {start|stop|reload| 
restart|configtest}"
RETVAL=1
esac
exit $RETVAL' > /etc/init.d/nginx

chkconfig --add /etc/init.d/nginx
chmod 755 /etc/init.d/nginx
chkconfig --add nginx
chkconfig nginx on
cd && rm -rf nginx*
exit 2
}




#卸载nginx
nginx_uninstall()
{
  ps -ef | grep nginx
  sleep 5
  systemctl stop nginx
  nginxdel=$(find / -name nginx | awk '$1')
  rm -rf $nginxdel
}

#运行函数
while :
do
	menu
done