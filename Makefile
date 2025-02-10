##########
# Docker #
##########

.PHONY: d-up
d-up:
	docker compose up -d

.PHONY: d-down
d-down:
	docker compose down

.PHONY: d-restart
d-restart:
	docker compose restart

.PHONY: d-python
d-python:
	docker compose exec python-trajectory bash

##############
# Trajectory #
##############

.PHONY: server
server:
	docker compose run --rm -p 3001:5000 -w /code python-trajectory python server.py

.PHONY: train
train:
	docker compose run --rm -w /code python-trajectory python train.py

.PHONY: tensorboard
tensorboard:
	docker compose run --rm -p 3002:6006 -w /code python-trajectory tensorboard --logdir tensorboard --bind_all

.PHONY: tests
tests:
	docker compose run --rm -w /code python-trajectory python -m unittest discover . "*Test.py"
