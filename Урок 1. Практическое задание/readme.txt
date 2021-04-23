
sudo apt-get install python3-pip
pip3 install uwsgi

uwsgi --http :8000 --wsgi-file run_no_wsgiref.py

gunicorn --workers=2 run_no_wsgiref:application --bind=0.0.0.0:8000