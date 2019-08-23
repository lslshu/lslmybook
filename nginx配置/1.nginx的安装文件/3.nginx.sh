#!/bin/bash
yum install gcc gcc-c++ pcre pcre-devel zlib zlib-devel openssl openssl-devel -y
groupadd www
useradd -g www www
wget http://nginx.org/download/nginx-1.14.2.tar.gz
tar -zxvf nginx-1.14.2.tar.gz
cd nginx-1.14.2 
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
