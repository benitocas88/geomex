build:
	docker build -t ebe/geomex:latest .

yarn: build
	docker run -it --rm \
	--volume $(CURDIR)/src:/opt/geomex \
	--workdir /opt/geomex/static \
	ebe/geomex:latest yarn install

webpack: yarn
	docker run -it --rm \
	--name geopack \
	--volume $(CURDIR)/src:/opt/geomex \
	--workdir /opt/geomex/static \
	ebe/geomex:latest npx webpack --watch --mode=development

up:
	docker-compose up -d

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
