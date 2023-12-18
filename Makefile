.PHONY: dev build-dev exec-backend

build-dev:
	docker-compose build

dev:
	docker-compose up

exec-backend:
	docker exec -it mg-backend bash
