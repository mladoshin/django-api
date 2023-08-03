#install python
apt update
apt install python3
apt install python3-pip

#create virtual envirinment
python3 -m venv env

#activate virtual env
chmod 777 env/bin/activate
env/bin/activate

#install packages
chmod 777 env/bin/pip
env/bin/pip install -r requirements.txt

#install nginx
apt install nginx

# copy gunicorn socket and service files
rm -f /etc/systemd/system/gunicorn.socket
rm -f /etc/systemd/system/gunicorn.service
cp ./gunicorn.socket /etc/systemd/system/
cp ./gunicorn.service /etc/systemd/system/

sudo systemctl daemon-reload

# start gunicorn socket
systemctl start gunicorn.socket

#enable gunicorn socket
systemctl enable gunicorn.socket

#check socket status
systemctl status gunicorn.socket

#check gunicorn status
systemctl status gunicorn

#reload daemon
systemctl daemon-reload

#restart gunicorn
systemctl restart gunicorn

#copy nginx config file
sudo cp --f ./api.nginx.conf /etc/nginx/sites-available/api


#create a link
sudo unlink /etc/nginx/sites-enabled/api
ln -s /etc/nginx/sites-available/api /etc/nginx/sites-enabled

#test nginx config
nginx -t

#restart nginx
sudo systemctl restart nginx

# block port 8000
sudo ufw delete allow 8000

#allow ports for nginx
sudo ufw allow 'Nginx Full'