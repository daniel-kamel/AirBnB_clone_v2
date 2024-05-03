#!/usr/bin/env bash
# Sets up your web servers for the deployment of web_static

# install nginx if not installed
sudo apt-get -y update
sudo apt-get -y install nginx

# Set up folders and files
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of /data folder to ubuntu user and group
sudo chown -hR ubuntu:ubuntu /data

# Configure Nginx to serve the content of /data/web_static/current/ to /hbnb_static route
echo "server {
  listen 80 default_server;
  listen [::]:80 default_server;
  add_header X-Served-By $HOSTNAME;
  root /var/www/html;
  index index.html index.htm;
  location /hbnb_static {
    alias /data/web_static/current;
    index index.html index.htm;
  }
}" | sudo tee /etc/nginx/sites-available/default

# Restart Nginx
sudo service nginx restart
