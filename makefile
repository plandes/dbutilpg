#@meta {desc: "Python build configuration", date: "2025-12-31"}


## Build system
#
#
# type of project
PROJ_TYPE =		python
PROJ_MODULES =		python/doc python/package python/deploy
PY_TEST_PRE_TARGETS =	testup
CLEAN_DEPS +=		down dkcleanall


## Project
#
POSTGRES_DIR ?=		postgres



## Includes
#
include ./zenbuild/main.mk


# install the postgres client Python library on macOS
.PHONY:		macosdep
macosdep:
		brew install libpq
		brew install --with-clang llvm
		CC="$$(brew --prefix llvm@11)/bin/clang" \
			PATH="$$PATH:$(brew --prefix libpq)/bin" \
			pip install 'psycopg2~=2.9.9'

## Docker
#
.PHONY:		up
up:
		@$(MAKE) $(PY_MAKE_ARGS) -C $(POSTGRES_DIR) up

.PHONY:		down
down:
		@$(MAKE) $(PY_MAKE_ARGS) -C $(POSTGRES_DIR) down || true

.PHONY:		dkcleanall
dkcleanall:
		@$(MAKE) $(PY_MAKE_ARGS) -C $(POSTGRES_DIR) cleanall rmvol

.PHONY:		testup
testup:		up
		sleep 2
