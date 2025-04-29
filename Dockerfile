# Use an official lightweight Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port used by the app
EXPOSE 8080

# Start the application using gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "main:app"]
