
sudo apt-get install python3-pip
pip3 install uwsgi

uwsgi --http :8002 --wsgi-file main.py

gunicorn --workers=2 main:application --bind=0.0.0.0:8002