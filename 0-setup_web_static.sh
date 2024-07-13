#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static

if [ -x "$(command -v nginx)" ]; then
	echo "nginx already installed"

else
       	echo "Installing nginx ..."
	sudo apt-get update
	sudo apt-get install nginx -y

fi 

# Create directory files

mkdir -p /data/web_static/{releases/test,shared}

# Create fake html file

echo "<html><body>Test page</body></html>" > /data/web_static/releases/test/index.html

# Create a symbolic link or recreate a symbolic link if one exists

ln -sf /data/web_static/releases/test /data/web_static/current

# Change ownership of the data file to ubuntu

sudo chown -R ubuntu:ubuntu /data/

# Update nginx configuration

sed -i '/server_name _;/a \\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default

service nginx restart
