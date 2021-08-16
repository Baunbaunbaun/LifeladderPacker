# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim-buster

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

# Install pip requirements
ADD /dist/lifeladderpacking-1.0.11-py3-none-any.whl .
RUN pip install --upgrade /lifeladderpacking-1.0.11-py3-none-any.whl
ADD requirements.txt .
RUN python -m pip install --upgrade -r requirements.txt

WORKDIR /app
ADD . /app

# Switching to a non-root user, please refer to https://aka.ms/vscode-docker-python-user-rights
RUN useradd appuser && chown -R appuser /app
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["waitress-serve", "--call", "lifeladderpacking:create_app"]