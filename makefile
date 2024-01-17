build-nest:
	docker build -t nestpy:0.1.0 .

bash:
	docker run --rm \
	-p 3000:3000 \
	-w /app \
	-v ${PWD}:/app \
	-it nestpy:0.1.0 bash

flake8:
	docker run --rm \
	-p 3000:3000 \
	-w /app \
	-v ${PWD}:/app \
	-it nestpy:0.1.0 poetry run flake8

black:
	docker run --rm \
	-p 3000:3000 \
	-w /app \
	-v ${PWD}:/app \
	-it nestpy:0.1.0 poetry run black nest

mypy:
	docker run --rm \
	-p 3000:3000 \
	-w /app \
	-v ${PWD}:/app \
	-it nestpy:0.1.0 poetry run mypy nest
