COMPOSE = docker compose

build:
	$(COMPOSE) build

npm: build
	docker run -it --rm \
	--volume $(CURDIR)/src:/home/userapp/src \
	--workdir /home/userapp/src/static \
	ebe/geomex:latest npm install

webpack-dev: npm
	docker run -it --rm \
	--name geopack \
	--volume $(CURDIR)/src:/home/userapp/src \
	--workdir /home/userapp/src/static \
	ebe/geomex:latest webpack --watch --mode=development

up: build
	$(COMPOSE) up -d --remove-orphans

down:
	$(COMPOSE) down --remove-orphans

rm: down
	docker rm $(shell docker ps -aq --filter name='geo*')

restart:
	$(COMPOSE) restart

upgrade:
	$(COMPOSE) exec geoapp flask db upgrade

console:
	$(COMPOSE) exec geoapp bash

migrate:
	$(COMPOSE) exec geoapp bash -c "flask db upgrade"

logs:
	$(COMPOSE) logs -tf

PHONY: run-deps
run-deps:
	$(COMPOSE) run --rm -it geoapp sh /opt/scripts/run-deps.sh $(args)
