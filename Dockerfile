FROM python:3.12-slim
WORKDIR /app
COPY . .
# Install BOTH Flask (for the app) and Pytest (for the pipeline)
RUN pip install flask pytest
EXPOSE 5000
CMD ["python", "app.py"]
