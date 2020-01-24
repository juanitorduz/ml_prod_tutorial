# ML in Production Tutorial

The idea to write up this repository is motivated by the very interesting set of blog posts from [http://mlinproduction.com/](http://mlinproduction.com/) by [Luigi](mailto:luigi@mlinproduction.com). In particular, the ones about dockerizing a machine learning models:

  - [Docker for Machine Learning – Part I](https://mlinproduction.com/docker-for-ml-part-1/)
  - [Docker for Machine Learning – Part II](https://mlinproduction.com/docker-for-ml-part-2/)
  - [Docker for Machine Learning – Part III](https://mlinproduction.com/docker-for-ml-part-3/)
  - [Using Docker to Generate Machine Learning Predictions in Real Time](https://mlinproduction.com/docker-for-ml-part-4/).

**Disclaimer:** The core of this repository is based on this reference and I encourage everyone to read them before going into the code if you do not have much experience on this topic.

In addition to the main functionalities, I also wanted to complement it with extra features which are not discussed there:

  - Train the machine learning model with data stored in an AWS S3 bucket. In particular, when building the Docker image, do not copy the training data into it.

  - Describe how to build a Docker image passing the credentials as `ARG` variables and not as `ENV` variables. This is particular special for security reasons.

  - Set up a [Docker container GitHub Action](https://help.github.com/en/actions/automating-your-workflow-with-github-actions/creating-a-docker-container-action) which gets trigger on `push`, which ensures reliability of your version control. 

![Build](https://github.com/juanitorduz/ml_prod_tutorial/workflows/Docker%20Image%20CI/badge.svg)

In this repository I explore tips and tricks to deploy machine learning models with Docker following [http://mlinproduction.com/](http://mlinproduction.com/) posts.

## Setup

1. Create virtual environment:
```bash
make env
```

2. Activate environment and install python packages:
```bash
make install
```

## Generate Data

```bash
make generate_data
```

## Train Model

```bash
make train
```

---

## Build Docker image
```bash
make docker_build
```

## API

Run docker container:
```bash
docker run -it -p 5000:5000 docker-model python api.py
```

Request predictions (example):
```bash
curl -i -H "Content-Type: application/json" -X POST -d '{"x": 1.2}' 127.0.0.1:5000/predict
```
