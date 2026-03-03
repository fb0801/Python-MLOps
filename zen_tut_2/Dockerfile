FROM jupyter/base-notebook:python-3.10

USER root

COPY requirements.txt .

RUN python -m pip install --no-cache-dir -r requirements.txt

USER $NB_UID
