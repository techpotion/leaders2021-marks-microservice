<img src="https://leaders2021.innoagency.ru/static/img/general/logo.svg"
  style="height: 80px;">

# Sport Object Analysis

## Depolyment
1. Clone repository and "cd" in it
```bash
$ git clone https://github.com/techpotion/leaders2021-data-science.git
$ cd leaders2021-data-science
```

2. Make virtual environment (optional) and install project's dependencies
```bash
$ python3 -m venv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

3 Run the project
```bash
$ python main.py
```

## Depolyment using Docker
1. Clone repository and "cd" in it
```bash
$ git clone https://github.com/techpotion/leaders2021-data-science.git
$ cd leaders2021-data-science
```

2. Build the docker image
```bash
$ docker build --tag microservice .
```

3. Run the project
```bash
$ docker run -d -p 3300:3300 --name techpotion-leaders2021-microservice microservice
```