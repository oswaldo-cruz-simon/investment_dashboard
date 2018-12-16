# Investment Dashboard
It is a project that helps to optimize a budget for investments, It allows to compare offerings based on crowdfunding platforms.
supported Platforms:
* Briq
* cumplo
* m2crowd
* inverspot

## Installation

### Create virtual environment
using Anaconda
~~~
conda create --name invdash python=3.6
source activate invdash
~~~
or using virtualenv
~~~
virtualenv -p /usr/bin/python3.6 environment
source activate environment
~~~
### Download selenium driver
~~~
wget https://chromedriver.storage.googleapis.com/2.40/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
rm chromedriver_linux64.zip
~~~

### Configurate credentials
1. copy and rename the file dotcredentials.yaml `cp dotcredentials.yaml .credentials.yaml`
2. open the file .credentials.yaml
3. replace users and passwords by valid ones for each site
