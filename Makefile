build:
	docker-compose build
	# docker build -t ebe/geomex:latest .

yarn: build
	docker run -it --rm \
	--volume $(CURDIR)/src:/home/userapp/src \
	--workdir /home/userapp/src/static \
	ebe/geomex:latest yarn install

webpack-dev: yarn
	docker run -it --rm \
	--name geopack \
	--volume $(CURDIR)/src:/home/userapp/src \
	--workdir /home/userapp/src/static \
	ebe/geomex:latest webpack --watch --mode=development

up:
	docker-compose up -d --build

stop:
	docker stop $(shell docker ps -aq --filter name='geo*')

rm: stop
	docker rm $(shell docker ps -aq --filter name='geo*')

restart:
	docker-compose restart

restore:
	cat geomex.sql | docker exec -i geomaria mysql -u root --password=secret geomex

upgrade:
	docker-compose exec geoapp flask db upgrade

console:
	docker-compose run geoapp bash

migrate:
	docker-compose exec geoapp bash -c "flask db upgrade"

logs:
	docker-compose logs -tf
