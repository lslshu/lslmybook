#！bin/bash
#切割nginx日志，需先创建backup
#日志保存位置
base_path='/backup/nginx/logs'
#备份年月日文件
mkdir -p /backup/nginx/logs$(date +%Y)$(date +%m)$(date +%d)
#备份日志文件到相应的
mv /usr/local/nginx/logs/access.log /backup/nginx/logs/$(date +%Y)$(date +%m)$(date +%d)/access_$(date -d "yesterday" +"%Y%m%d").log
mv /usr/local/nginx/logs/error.log /backup/nginx/logs/$(date +%Y)$(date +%m)$(date +%d)/error_$(date -d "yesterday" +"%Y%m%d").log
mv /usr/local/nginx/logs/jx.access.log /backup/nginx/logs/$(date +%Y)$(date +%m)$(date +%d)/jx.access_$(date -d "yesterday" +"%Y%m%d").log
mv /usr/local/nginx/logs/video.access.log /backup/nginx/logs/$(date +%Y)$(date +%m)$(date +%d)/video.access_$(date -d "yesterday" +"%Y%m%d").log
mv /usr/local/nginx/logs/www.access.log /backup/nginx/logs/$(date +%Y)$(date +%m)$(date +%d)/www.access_$(date -d "yesterday" +"%Y%m%d").log
# 通过Nginx信号量控制重读日志
kill -USR1 `cat /usr/local/nginx/logs/nginx.pid`

#crontab -e 配置定时任务，比如每天23:55备份
#59  23  * * * /backup/nginx/nginx_backup.sh
