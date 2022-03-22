IMAGE_NAME=authz
IMAGE_TAG=latest
GIT_COMMIT := $(shell git rev-parse HEAD)
GIT_TAG := $(shell git tag --points-at HEAD)

.PHONY: all
all: install dev

.PHONY: install
install:
	apt update && apt install -y python3 python3-pip

.PHONY: dev
dev:
	apt update && apt install -y python3-venv
	
.PHONY: build
build:
	docker build -t ${IMAGE_NAME}:${IMAGE_TAG} --build-arg GIT_COMMIT=${GIT_COMMIT} --build-arg GIT_TAG=${GIT_TAG} .
