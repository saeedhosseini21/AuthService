.PHONY: all
all: install dev

.PHONY: install
install:
	apt update && apt install -y python3 python3-pip

.PHONY: dev
dev:
	apt update && apt install -y python3-venv
