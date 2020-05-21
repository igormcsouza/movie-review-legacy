FROM python:3

RUN /usr/local/bin/python -m pip install --upgrade pip

RUN pip install Flask==1.1.2
RUN pip install gunicorn==19.9.0
RUN pip install scikit-learn==0.22.2

WORKDIR /api

COPY api /api
COPY models /models

CMD gunicorn app:app