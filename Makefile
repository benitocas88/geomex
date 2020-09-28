build:
	docker-compose build

up: build
	docker-compose up -d

geo:
	docker-compose exec geoscript flask geo

stop:
	docker-compose stop

restart:
	docker-compose restart
