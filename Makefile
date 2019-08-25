all:

build:
	cd frontend; yarn install; yarn run build; cd ..;

run: build
	gunicorn -b 127.0.0.1:8080 -k geventwebsocket.gunicorn.workers.GeventWebSocketWorker main:app

deploy:
	echo 'deploy'
