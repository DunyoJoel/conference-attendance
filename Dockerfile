FROM python:3.10.4-slim-buster

# 
WORKDIR /app


# Set up Python behaviour
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV VIRTUAL_ENV=/opt/venv

# Switch on virtual environment
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Set the server port
EXPOSE 8000

# Install system dependencies
RUN apt-get update && \
    apt-get install -yqq build-essential gcc && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get clean

# Install Python dependencies
RUN pip3 install --upgrade pip
COPY ./requirements.txt ./
RUN pip3 install -r requirements.txt


# Copy all files
COPY . /app

# Start up the backend server
# CMD [ "uvicorn", "app.main:app", "--workers", "4", "--host", "0.0.0.0", "--port", "5000" ]
