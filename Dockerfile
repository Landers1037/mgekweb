FROM python:3.7
MAINTAINER Landers liaorenj@gmail.com
WORKDIR /mgek
ADD . /mgek
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 1317
CMD ["gunicorn", "-c", "gun.py", "app:app"]