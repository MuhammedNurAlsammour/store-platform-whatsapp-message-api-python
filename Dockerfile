# Use Python 3.9 slim base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    xvfb \
    x11vnc \
    xauth \
    firefox-esr \
    xfonts-base \
    x11-utils \
    python3-tk \
    python3-dev \
    libpci3 \
    libegl1 \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libnss3 \
    libxcb1 \
    libxcomposite1 \
    libxcursor1 \
    libxdamage1 \
    libxfixes3 \
    libxi6 \
    libxrandr2 \
    libxrender1 \
    libxss1 \
    libxtst6 \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create necessary directories and files
RUN mkdir -p /app/logs \
    && mkdir -p /tmp/.X11-unix \
    && chmod 1777 /tmp/.X11-unix \
    && touch /root/.Xauthority

# Set environment variables
ENV DISPLAY=:99
ENV PYTHONUNBUFFERED=1
ENV MOZ_HEADLESS=1
ENV GECKO_DRIVER_PATH=/usr/local/bin/geckodriver

# Create entrypoint script with improved X server handling
RUN echo '#!/bin/bash\n\
# Setup X11 authentication\n\
xauth add :99 MIT-MAGIC-COOKIE-1 $(mcookie)\n\
\n\
# Remove any existing locks\n\
rm -f /tmp/.X99-lock\n\
\n\
# Start Xvfb with larger screen and more features\n\
Xvfb :99 -screen 0 1920x1080x24 -ac +extension GLX +render -noreset &\n\
\n\
# Wait for Xvfb to start\n\
for i in $(seq 1 10); do\n\
    if xdpyinfo -display :99 >/dev/null 2>&1; then\n\
        break\n\
    fi\n\
    echo "Waiting for Xvfb to start..."\n\
    sleep 1\n\
done\n\
\n\
# Start the Python application\n\
exec python app.py' > /app/entrypoint.sh \
    && chmod +x /app/entrypoint.sh

# Expose port
EXPOSE 5000

# Set entrypoint
ENTRYPOINT ["/app/entrypoint.sh"]