<img src="https://leaders2021.innoagency.ru/static/img/general/logo.svg"
  style="height: 80px;">

# Sport Object Analysis

## Depolyment
1. Clone repository and "cd" into it
```bash
$ git clone https://github.com/techpotion/leaders2021-marks-microservice.git
$ cd leaders2021-marks-microservice
```

2. Make virtual environment (optional) and install project's dependencies
```bash
$ python3 -m venv env
$ source env/bin/activate
$ pip install -r production_requirements.txt
```

3 Run the project
```bash
$ python main.py
```

## Depolyment using Docker
1. Clone repository and "cd" into it
```bash
$ git clone https://github.com/techpotion/leaders2021-marks-microservice.git
$ cd leaders2021-marks-microservice
```

2. Build the docker image
```bash
$ docker build --tag leaders2021-marks-microservice .
```

3. Run the project
```bash
$ docker run -d -p 3300:3300 --name leaders2021-marks-microservice leaders2021-marks-microservice
```
