## makefile automates the build and deployment for python projects

# type of project
PROJ_TYPE=		python
POSTGRES_DIR ?=		postgres
CLEAN_ALL_DEPS +=	dkcleanall

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
		make -C $(POSTGRES_DIR) down

.PHONY:		dkcleanall
dkcleanall:
		make -C $(POSTGRES_DIR) cleanall

.PHONY:		testup
testup:		up
		sleep 5

# primary test target
.PHONY:		testdocker
testdocker:	testup
		src/bin/testdb.sh
