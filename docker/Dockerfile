FROM python:3.8-slim

MAINTAINER Ilya Basharov <ilya.basharov.98@mail.ru>

ARG USER=online_inference
ARG UID=1000
ARG GID=1000
# default password
ARG PW=user

RUN useradd -m ${USER} --uid=${UID} && \
	echo "${USER}:${PW}" | chpasswd && \
	adduser ${USER} sudo

WORKDIR /home

RUN chown -R ${UID}:${GID} ./

COPY --chown=${USER}:${USER} . .

RUN python3 -m pip install --no-cache-dir --upgrade pip && \
	python3 -m pip install --no-cache-dir --upgrade setuptools && \
	python3 -m pip install -r ${USER}/requirements.txt && \
	rm -rf /var/lib/apt/lists/*

USER ${UID}:${GID}