FROM --platform=linux/amd64 faucet/python3
WORKDIR /app
COPY requirements.txt .
COPY app .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD [ "python3", "main.py" ]

