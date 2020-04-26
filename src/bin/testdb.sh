#!/bin/sh

export NLP_SERV=localhost
export NLP_PORT=5432
export NLP_USER=sa
export NLP_PASS=sa1234

make test
