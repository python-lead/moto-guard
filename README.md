<h1 align="center">
  <br>
  <br>
  moto-guard
  <br>
</h1>

<h4 align="center">Django based motorcycle service tracker</h4>
<h5 align="center">"Set reminders and stay ahead of maintenance schedules. A rider's companion for a smoother, worry-free journey on two wheels"</h5>
<h6 align="center"> - GPT-3.5</h6>

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Other](#other)


## General info
This project is a sandbox for me to play with a small API based app while also testing and utilising good practices 
that I've learned from working on different Django projects

## Technologies
#### Project environment:
* Docker: 20.10.7
* docker-compose: 1.29.2

#### Project backend service:
* Python: 3.12.2
* Django: ~4.2

## Requirements:
* Docker: ^24.0.2
* docker-compose: ^2.18.1
#### Optional:
* make

## Setup
To run this project locally cd into the project and:

```
$ make build-dev
# Builds docker containers

$ make dev
# Starts containers for local development

$ make exec-backend
# enters backend container shell via bash
```

## Other:

### Pre-commit hooks:
#### backend hooks:
- Formats /backend/src using black
- Executes mypyc-compiled black format check

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
