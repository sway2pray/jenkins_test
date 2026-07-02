FROM python:3.9-slim
RUN groupadd -g 10001 appgroup && \
    useradd -r -u 10001 -g appgroup -m -s /bin/bash appuser

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY --chown=appuser:appgroup . .
CMD ["python", "app.py"]