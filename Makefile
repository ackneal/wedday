all:

build:
	cd frontend; yarn install; yarn run build; cd ..;

run: build
	gunicorn -b 127.0.0.1:8080 -k eventlet -w 1 main:app

deploy: build
	gcloud beta app deploy
