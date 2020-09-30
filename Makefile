build:
	docker-compose build

yarn: build
	docker-compose exec -w /app/src/static geoapp yarn install --silent

up: build
	docker-compose up -d

geo:
	docker-compose exec geoapp flask geo

stop:
	docker-compose stop

restart:
	docker-compose restart

georestore:
	cat geomex.sql | docker exec -i geomaria mysql -u root --password=secret geomex

webpack: yarn
	docker-compose exec -w /app/src/static geoapp yarn run webpack-dev
