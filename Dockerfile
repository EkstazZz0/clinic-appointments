FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY app .

ENV TZ=UTC
RUN ln -sf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get update && apt-get install -y --no-install-recommends libpq-dev

ARG APP_HOST
ARG APP_PORT

ENV APP_HOST=${APP_HOST}
ENV APP_PORT=${APP_PORT}

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]