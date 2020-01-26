# ML in Production Tutorial

![Build](https://github.com/juanitorduz/ml_prod_tutorial/workflows/Docker%20Image%20CI/badge.svg) ![Build](https://github.com/juanitorduz/ml_prod_tutorial/workflows/Pytest%20CI/badge.svg) [![codecov](https://codecov.io/gh/juanitorduz/ml_prod_tutorial/branch/master/graph/badge.svg)](https://codecov.io/gh/juanitorduz/ml_prod_tutorial)

The idea to write up this repository is motivated by the very interesting set of blog posts from [http://mlinproduction.com/](http://mlinproduction.com/) by [Luigi Patruno](mailto:luigi@mlinproduction.com). In particular, the ones about dockerizing a machine learning models:

  - [Docker for Machine Learning – Part I](https://mlinproduction.com/docker-for-ml-part-1/)
  - [Docker for Machine Learning – Part II](https://mlinproduction.com/docker-for-ml-part-2/)
  - [Docker for Machine Learning – Part III](https://mlinproduction.com/docker-for-ml-part-3/)
  - [Using Docker to Generate Machine Learning Predictions in Real Time](https://mlinproduction.com/docker-for-ml-part-4/).

**Disclaimer:** The core of this repository is based on this reference and I encourage everyone to read them before going into the code if you do not have much experience on this topic.

In addition to the main functionalities, I also wanted to complement it with extra features which are not discussed there:

  - Train the machine learning model with data stored in an [AWS S3 bucket](https://aws.amazon.com/s3/). In particular, when building the Docker image, do not copy the training data into it.

  - Describe how to build a Docker image passing the credentials as `ARG` variables and not as `ENV` variables. This is particular special for security reasons.
  
  - Unit Testing (needs more tests).

  - Set up [GitHub Actions](https://github.com/features/actions):
    - [Docker container GitHub Action](https://help.github.com/en/actions/automating-your-workflow-with-github-actions/creating-a-docker-container-action)
    - [Python (pytest) Action](https://help.github.com/en/actions/automating-your-workflow-with-github-actions/using-python-with-github-actions)
    - [Codecov GitHub Action](https://github.com/codecov/codecov-action) to get reports on tests coverage. 

    which get trigger on `push`, which ensures reliability on the code.

  - Deploy to EC2 (#TODO) via cloud formation/terraform.

I have also added a [Resources](https://github.com/juanitorduz/ml_prod_tutorial/blob/master/resources.md) section where I store useful references, interesting reading and similar approaches.

**Remark:** This repository structure should be seen as a *toy-use-case*. You might want to package the files correctly, using for example [Cookiecutter Data Science](https://drivendata.github.io/cookiecutter-data-science/).

---
## Contributing

I will keep adding functionalities to this *toy model* repository. If you have some other relevant resources, suggestions, comments or find bugs please create a Pull Request or [drop me a line](mailto:juanitorduz@gmail.com).

---
## Setup

We are going to use a [Makefile](https://www.gnu.org/software/make/manual/html_node/Introduction.html) for the main functionalities.

1. Create virtual environment:

```bash
make venv
```

2. Activate environment and install python packages:

```bash
make install
```

## Generate Data

This toy-model example fits a linear regression model of the form y ~ x. To generate  sample data for this model you can run the command (writes it to `data/train_data.csv`

```bash
make generate_data
```

To train the model store the training data in a **secure** S3 bucket.

## Train Model

To train and save the model (to `model/ml_mod.joblib`, see `envs.py`) run:

```bash
make train
```

The training phase assumes the data is stored in an S3 bucket with relative path: `s3://S3BUCKET/ml_prod_tutorial/data/train_data.csv`.

---

## AWS Credentials

It is recommended to create an [IAM User](https://aws.amazon.com/iam/) with the appropriate credentials. You can store the `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY` and the `AWS_REGION` as environmental variables using the `aws configure` command from the [`aws cli`](https://aws.amazon.com/cli/). For this repository I am assuming the *default* profile.

**Warning:** never store your credentials in any script on a GitHub repository!

---
## Build Docker image

To build the docker image simply run:

```bash
make docker_build
```

This image trains and saves the model in order to generate predictions. You can test it by generate predictions on sample data by running the command:

```bash
docker run docker-model inference.py
```

## Flask App

The module `apy.py` defines a [Flask](https://flask.palletsprojects.com/en/1.1.x/) application which enable us to generate prediction in real time. To spin up the app just run (we choose `port = 5000`):

Run docker container:
```bash
docker run -it -p 5000:5000 docker-model python api.py
```

To generate prediction for a given sample data point (here, x = 1.2 )you can run (locally):

```bash
curl -i -H "Content-Type: application/json" -X POST -d '{"x": 1.2}' 127.0.0.1:5000/predict
```

---
## Docker container GitHub Action

In this step we set up a Docker container GitHub Action where we test the Docker image build on each push. Note that this requires training the model (this could or could not be ideal, depends on the application), which in particular requires access to the data. As stressed above, we do not want to store the AWS credentials on the repository. One option it to store them as [GitHub Secrets](https://help.github.com/en/actions/automating-your-workflow-with-github-actions/creating-and-using-encrypted-secrets). When could then access them using, for example, `${{secrets.AWS_ACCESS_KEY_ID}}`.
