#!/bin/bash

docker build . \
    -f docker/Dockerfile \
    -t ilyabasharov/made_mail.ru \
    --build-arg UID=${UID} \
    --build-arg GID=${UID} 
