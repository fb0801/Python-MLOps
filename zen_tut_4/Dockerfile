FROM jupyter/base-notebook:python-3.10

USER root

# System deps
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Upgrade tooling
RUN python -m pip install --upgrade pip setuptools wheel

# ✅ ADD THIS LINE (fixes PyYAML build)
RUN python -m pip install cython

COPY requirements.txt .

RUN python -m pip install -r requirements.txt

USER $NB_UID
