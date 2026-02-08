FROM python:3.9

# টাইমজোন সেট করার জন্য
ENV TZ="Asia/Kolkata"

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]
