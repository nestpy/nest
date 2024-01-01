build-poetry:
	docker build -t poetry:1.7.1 .

bash:
	docker run --rm \
	-p 3000:3000 \
	-w /app \
	-v ${PWD}:/app \
	-it poetry:1.7.1 bash
