## LocalStack Issue

This repo can be used to reproduce an issue found in LocalStack using CDK for deployment.

### Repro Steps

1. Install python 3.8
    a. `pyenv install 3.8`
2. Activate python 3.8
    a. `pyenv shell 3.8`
3. `cdklocal bootstrap`
4. `cdklocal deploy`