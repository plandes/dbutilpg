## makefile automates the build and deployment for python projects

# type of project
PROJ_TYPE=		python
PROJ_MODULES=		git python-doc python-doc-deploy
POSTGRES_DIR ?=		postgres
CLEAN_DEPS +=		down
CLEAN_ALL_DEPS +=	dkcleanall
PY_TEST_DEPS +=		testup
PYTHON_TEST_ENV = 	NLP_SERV=localhost NLP_PORT=5432 NLP_USER=sa NLP_PASS=sa1234


include ./zenbuild/main.mk


.PHONY:		macosdep
macosdep:	pydeps
		brew install libpq
		PATH="$(brew --prefix libpq)/bin:$PATH" pip install psycopg2==2.8.3

.PHONY:		up
up:
		make -C $(POSTGRES_DIR) up

.PHONY:		down
down:
		make -C $(POSTGRES_DIR) down || true

.PHONY:		dkcleanall
dkcleanall:
		make -C $(POSTGRES_DIR) cleanall

.PHONY:		testup
testup:		up
		sleep 1
