FROM jupyter/base-notebook:python-3.10

USER root

COPY requirements.txt .

RUN python -m pip install requirements.txt

USER $NB_UID
