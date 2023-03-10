FROM python:3.10.4

# 
WORKDIR /code


# Set up Python behaviour
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV VIRTUAL_ENV=/opt/venv

# Switch on virtual environment
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Set the server port
EXPOSE 5000

# Install system dependencies
RUN apt-get update && \
    apt-get install -yqq build-essential gcc && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get clean

# Install Python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt ./
RUN pip install -r requirements.txt


# Copy all files
COPY . .

# Start up the backend server
CMD [ "uvicorn", "app.main:app", "--workers", "4", "--host", "0.0.0.0", "--port", "5000" ]
