FROM python:3.12-slim
WORKDIR /Myapp
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "Myapp.py"]
EXPOSE 5000