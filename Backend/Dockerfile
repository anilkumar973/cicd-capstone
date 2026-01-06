# -------- BUILD STAGE --------
FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user -r requirements.txt

# -------- RUNTIME STAGE --------
FROM python:3.11-slim
RUN useradd -m appuser
WORKDIR /app

COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

COPY app.py migrate.py ./

USER appuser
EXPOSE 5000

CMD ["python", "app.py"]
