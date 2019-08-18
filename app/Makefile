all:

deploy:
	yarn install; yarn run build
	cp app.yaml dist/; cd dist; gcloud app deploy; cd -; rm -rf dist
