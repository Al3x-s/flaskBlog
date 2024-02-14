FROM --platform=linux/amd64 faucet/python3
WORKDIR /application
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD [ "python3", "main.py" ]

