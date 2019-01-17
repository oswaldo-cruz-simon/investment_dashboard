FROM python:3.6
# install google chrome
# copied from https://github.com/joyzoursky/docker-python-chromedriver/blob/master/py3/py3.6/Dockerfile
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable

ENV DISPLAY=:99
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

# ENTRYPOINT echo "Invesment analytic are running now!!"
