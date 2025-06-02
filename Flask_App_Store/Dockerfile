FROM python:3.11
EXPOSE 5000
WORKDIR /app
COPY requirement.txt .
RUN pip install -r requirement.txt
COPY . /app
CMD ["flask","run","--host","0.0.0.0"]