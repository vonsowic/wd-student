#!/bin/bash

dir=`pwd`
 
# install python3.6.0
wget https://www.python.org/ftp/python/3.6.0/Python-3.6.0.tar.xz --no-check-certificate
tar xf Python-3.6.0.tar.xz
rm Python-3.6.0.tar.xz
mv Python-3.6.0/ tmp_python
cd tmp_python
find ./ -type d | xargs chmod 0755
configure --prefix=$HOME/Python
make && make install
cd ..
rm -rf ${dir}/tmp_python 

# configure program
$HOME/Python/bin/python3 ${dir}/main.py
echo "*/5 * * 1,2,6,7 * "$HOME"/Python/bin/python3 "${dir}"/main.py" > cron
crontab cron
rm cron
