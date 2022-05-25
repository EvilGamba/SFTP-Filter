apt isntall -y
apt install openssh-server
systemctl enable ssh
systemctl start ssh
groupadd sftp
mv sshd_config /etc/ssh/sshd_config
systemctl restart ssh

mkdir -p /opt/SFTP-Filter/Compiled/Scripts
mkdir /opt/SFTP-Filter/YARA_Rules/
mkdir /etc/SFTP-Filter
mkdir /bin/SFTP-Filter

cp bin/* /bin/SFTP-Filter
cp etc/* /etc/SFTP-Filter

cp service/SysMon.sh /bin/SFTP-Filter
cp service/uploadfilter.service /etc/systemd/system

chmod +x /bin/SFTP-Filter/SysMon.sh
systemctl enable uploadfilter.service


echo export PATH=$PATH:/bin/SFTP-Filter >> ~/.bashrc

reboot now
