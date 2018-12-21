up: down
	docker-compose up -d --build
	docker-compose logs -f

down:
	docker-compose down

build:
	docker-compose build

cameras: build
	docker-compose run app python cameras.py

test-snap:
	docker-compose run app python snap.py

timelapse:
	docker-compose run app ffmpeg -r 30 -pattern_type glob -i '/images/*.jpg'  -c:v libx264 -pix_fmt yuv420p /images/timelapse.mp4
