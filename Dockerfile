FROM python:alpine

# Create necessary dirs
RUN mkdir -p /app /data
WORKDIR /app

# Copy files
COPY generate_ics.py serve.py entrypoint.sh requirements.txt /app/

# Make output directory for ics file
RUN mkdir -p /app/data/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Make entrypoint executable
RUN chmod +x /app/entrypoint.sh

# Expose HTTP port
EXPOSE 8080

# Start the whole thing
ENTRYPOINT ["/app/entrypoint.sh"]
