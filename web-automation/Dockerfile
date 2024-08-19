FROM n8nio/n8n

# Set timezone to Warsaw for more accurate logging
ENV TZ="Europe/Warsaw"

# Install python/pip
ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools

# Install chromium
RUN apk -U add chromium udev ttf-freefont

COPY requirements.txt .

# Install Python libraries
RUN python -m pip install -r requirements.txt

# Set environment variables
ENV TV_USERNAME=$TV_USERNAME
ENV TV_PASSWORD=$TV_PASSWORD

# Copy remaining files (cache busts here)
COPY . .

# ENDPOINT command will be used from the original n8n image
