FROM python:3.9
WORKDIR /api/
COPY ./main.py /api/
CMD ["uvicorn", "main:start", "--host", "0.0.0.0", "--port", "80"]

