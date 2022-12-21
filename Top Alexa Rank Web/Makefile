.PHONY: build venv deps clean init ioweb

build: venv deps init

venv:
	virtualenv -p python3.5 .env

deps:
	.env/bin/pip install -r requirements.txt

clean:
	find -name '*.pyc' -delete
	find -name '*.swp' -delete
	find -name '__pycache__' -delete

init:
	if [ ! -e var/run ]; then mkdir -p var/run; fi
	if [ ! -e var/log ]; then mkdir -p var/log; fi

ioweb:
	mkdir src
	ln -s /web/ioweb src
	ln -s src/ioweb
	.env/bin/pip install -e src/ioweb
