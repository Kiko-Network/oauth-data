FROM python:3.10-slim
WORKDIR /app
COPY . /app/
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt
RUN chmod +x run.sh
EXPOSE 8000
CMD ["bash", "run.sh"]