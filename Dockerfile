FROM python:3.8-slim

# Copy over app and reqs
COPY src/ /app
COPY reqs/app.txt /app/

# Change workdir to our app folder
WORKDIR /app

# Add app folder to pypath
ENV PYTHONPATH "${PYTHONPATH}:/app"

# Install dependencies
RUN pip3 install -r /app/app.txt 

# Start application
CMD [ "uvicorn", "main:app", "--reload", "--host=0.0.0.0", "--port=8000"]

EXPOSE 8000
