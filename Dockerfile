FROM python:3.11-slim

LABEL maintainer="samzong.lu@gmail.com"

WORKDIR /app

# 安装 Poetry
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python3 - && \
    apt-get remove -y curl && apt-get autoremove -y && \
    ln -s $HOME/.local/bin/poetry /usr/local/bin/poetry

# 复制项目文件
COPY . .

# 安装项目依赖
RUN poetry install --no-dev

# 暴露端口
EXPOSE 5000

# 启动项目
CMD ["poetry", "run", "uvicorn", "main:app" ,"--host", "0.0.0.0", "--port", "5000"]
