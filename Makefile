all:

build:
	cd frontend; yarn install; yarn run build; cd ..;

run: build
	gunicorn -b localhost:8080 -k flask_sockets.worker main:app;

deploy:
	echo 'deploy'
