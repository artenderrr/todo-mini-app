FROM ubuntu:24.04

RUN apt update && apt upgrade -y
RUN apt install curl -y

RUN curl -LsSf https://astral.sh/uv/install.sh | sh

WORKDIR /app
COPY . .

EXPOSE 8000

CMD ["/root/.local/bin/uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]