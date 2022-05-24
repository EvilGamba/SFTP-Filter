useradd -m -g sftp $1
passwd $1
mkdir /home/$1/datadir
chown root /home/$1
chmod 755 /home/$1
chown $1 /home/$1/datadir
chmod 755 /home/$1/datadir