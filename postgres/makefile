## makefile automates the build and deployment for docker projects

# type of project, currently one of: clojure, python
PROJ_TYPE=		docker
DOCKER_UP_DEPS=		
CLEAN_ALL_DEPS=		rmvol


include ../zenbuild/main.mk


.PHONY:			rmvol
rmvol:			down
			$(DOCKER_CMD) volume rm postgres_test_data | true
