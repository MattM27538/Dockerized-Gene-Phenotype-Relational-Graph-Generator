FROM python:3.10

WORKDIR ./app

COPY . .

# Get tkinter to display plt figures.
RUN apt-get update && apt-get install -y python3-tk

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "main.py"]