### Note: Used python 3.9.9 in this project

# Install Python packages

```bash

pip3 install -r requirements.txt

# you can install requirements-dev.txt if you want to use debugger and some dev packages
pip3 install -r requirements-dev.txt

```

# Settings

- You can change some configuration about project like project name, version etc.

```
cp config-sample.ini config.ini

# Example
[FASTAPI]
PROJECT_NAME=Flatten Array Challenge
API_PREFIX=/api
API_VERSION=v.0.1
DEBUG=1
```


# How to run the project?

``` bash

uvicorn main:app --reload

```
