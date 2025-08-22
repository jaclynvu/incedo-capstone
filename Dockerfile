FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
# Copy app code and assets
COPY app/app.py .                     
COPY app/templates/ templates/      
COPY app/static/ static/            
COPY models/ models/             
EXPOSE 8080

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]