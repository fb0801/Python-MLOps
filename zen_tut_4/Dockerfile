FROM jupyter/base-notebook:python-3.10

USER root

# ✅ Install build tools needed for PyYAML and others
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# ✅ Upgrade pip + setuptools (VERY important)
RUN python -m pip install --upgrade pip setuptools wheel

COPY requirements.txt .

RUN python -m pip install -r requirements.txt

USER $NB_UID

