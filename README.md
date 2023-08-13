## LocalStack Issue

This repo can be used to reproduce an issue found in LocalStack using CDK for deployment.

### Requirements

- Docker
- Node
- `cdklocal` -- `npm install -g aws-cdk-local aws-cdk`
- python 3.8 -- `pyenv install 3.8`

### Repro Steps

- Update `docker-compose.yml` with your LocalStack Pro API Key
- Start LocalStack -- `docker-compose up`
- Activate python 3.8 -- `pyenv shell 3.8`
- `pip install -r requirements.txt`
- `cdklocal bootstrap`
- `cdklocal deploy`