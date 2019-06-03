# Investment Dashboard
It is a project that helps to optimize a budget for investments, It allows to compare offerings based on crowdfunding platforms.
supported Platforms:
* Briq
* cumplo
* m2crowd
* inverspot

## Getting Started

### Prerequisites
Selenium Driver
~~~
wget https://chromedriver.storage.googleapis.com/2.40/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
rm chromedriver_linux64.zip
~~~
### Installing
Using Anaconda
~~~
conda create --name invdash python=3.6
source activate invdash
pip install -r requirements.txt
~~~
Or using virtualenv
~~~
virtualenv -p /usr/bin/python3.6 env
source activate env
pip install -r requirements.txt
~~~

Configure credentials
1. copy and rename the file dotcredentials.yaml `cp dotcredentials.yaml .credentials.yaml`
2. open the file .credentials.yaml
3. replace users and passwords by valid ones for each site

### Run
Run scraper and send data to Kinesis.
First activate the virtualenv
~~~shell
python extract/scraper.py cumplo -l
python extract/scraper.py briq -l
~~~
Run Kinesis consumer
~~~shell
python extract/kinesis_consumer.py
~~~
### Deployment
~~~SHELL
docker build -t scraper:v1 .
docker run scraper:v1 briq -l
docker run scraper:v1 cumplo -l
~~~

## Authors

* **[Oswaldo Cruz Simon](https://github.com/OswaldoCuzSimon)**
* **[Isaac Fonseca](https://github.com/next-javierisaacfonseca)** 