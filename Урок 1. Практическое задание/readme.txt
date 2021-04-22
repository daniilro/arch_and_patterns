
sudo apt-get install python3-pip
pip3 install uwsgi

uwsgi --http :8000 --wsgi-file <filename>.py