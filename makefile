## makefile automates the build and deployment for python projects

# type of project
PROJ_TYPE=		python
PROJ_MODULES=		git python-doc python-doc-deploy

# project
POSTGRES_DIR ?=		postgres

# build
PY_DEP_POST_DEPS +=	macosdep
CLEAN_DEPS +=		down
CLEAN_ALL_DEPS +=	dkcleanall
PY_TEST_DEPS +=		testup
PYTHON_TEST_ENV = 	NLP_SERV=localhost NLP_PORT=5432 NLP_USER=sa NLP_PASS=sa1234


include ./zenbuild/main.mk


.PHONY:		macosdep
macosdep:
		brew install libpq
		PATH="$$(brew --prefix libpq)/bin:$$PATH" pip install psycopg2==2.8.3

.PHONY:		up
up:
		make -C $(POSTGRES_DIR) up

.PHONY:		down
down:
		make -C $(POSTGRES_DIR) down || true

.PHONY:		dkcleanall
dkcleanall:
		make -C $(POSTGRES_DIR) cleanall rmvol

.PHONY:		testup
testup:		up
		sleep 2
