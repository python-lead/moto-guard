.PHONY: dev build-dev exec-backend

build-dev:
	docker-compose build

dev:
	docker-compose up

exec-backend:
	docker-compose exec mg-backend bash
