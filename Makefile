
COMPOSE := docker-compose -f docker-compose.yml -f compose/docker-compose.dev.yml
COMPOSE_TEST := $(COMPOSE) -f compose/docker-compose.test.yml
COMPOSE_PROD := docker-compose -f docker-compose.yml -f compose/docker-compose.prod.yml

help:
	@echo
	@echo ----------------------------------------------------------------------
	@echo "   Development commands file                                        "
	@echo ----------------------------------------------------------------------
	@echo ">  R U N N I N G"
	@echo "  - build			            Build the containers for development"
	@echo "  - up			                Run & Up development server"
	@echo "  - clean			            Remove containers"
	@echo "  - create_network			    Create docker network to allow share resources"
	@echo "  - migrate			            Run migrate command"
	@echo "  - statics			            Run Collect statics command"
	@echo "  - superuser			        Create a superuser"
	@echo "  - coverage			            Run coverage report"


create_network:
	@echo "Create a docker network ..."
	docker network create django_network

build:
	@echo "Server django up..."
	$(COMPOSE_PROD) build

up:
	@echo "Server django up..."
	$(COMPOSE_PROD) up

clean:
	@echo "Cleaning containers ..."
	docker ps -aq | xargs docker stop
	docker ps -aq | xargs docker rm


migrations:
	@echo "Applying migrations ..."
	$(COMPOSE_PROD) run --rm django python manage.py makemigrations $(ARG)

migrate:
	@echo "Applying migrations ..."
	$(COMPOSE_PROD) run --rm django python manage.py migrate $(ARG)

superuser:
	@echo "Creating superuser..."
	$(COMPOSE_PROD) run --rm django python manage.py createsuperuser

statics:
	@echo "Collect statics ..."
	$(COMPOSE_PROD) run --rm django python manage.py collectstatic

test:
	@echo "Running tests with pytest cleaning cache..."
	$(COMPOSE_TEST) run --rm django pytest --pyargs $(ARG)

locales:
	@echo "Opening a shell session"
	$(COMPOSE_PROD) run --rm django python manage.py makemessages -l en
	$(COMPOSE_PROD) run --rm django python manage.py makemessages -l es_MX

compile_locales:
	@echo "Opening a shell session"
	$(COMPOSE_PROD) run --rm django python manage.py compilemessages

coverage:
	$(COMPOSE_TEST) run django coverage run -m pytest
	$(COMPOSE_TEST) run --rm django coverage html
	$(COMPOSE_TEST) run --rm django coverage report
	$(COMPOSE_TEST) run --rm django rm -f web/badges/coverage.svg
	$(COMPOSE_TEST) run --rm django coverage-badge -o web/badges/coverage.svg

flushdb:
	@echo "Flushing database ..."
	$(COMPOSE_PROD) run --rm django python manage.py flush
