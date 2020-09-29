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

css-build: yarn
	docker-compose exec -w /app/src/static geoapp yarn run css-build

css-dev: css-build
	docker-compose exec -w /app/src/static geoapp yarn run css-watch
