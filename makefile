.PHONY: build-nest bash server dev

build-nest:
	docker build -t nestpy:0.2.0 .

bash:
	docker run --rm \
	-p 3000:3000 \
	-w /app \
	-v ${PWD}:/app \
	-it nestpy:0.2.0 bash

server:
	docker run --rm \
	-p 8000:8000 \
	-w /app \
	-v ${PWD}:/app \
	nestpy:0.2.0 poetry run python -m nest.main

dev: build-nest server

  