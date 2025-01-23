# NOTES

## cmds

**Build image**

```sh
$ docker build --platform linux/amd64 -t defaultwesteuacr.azurecr.io/flask-app:latest .
$ docker run -p 80:5000 defaultwesteuacr.azurecr.io/flask-app:latest
```

**Deploy image**

```sh
$ az acr login --name defaultwesteuacr
$ az acr update -n defaultwesteuacr --admin-enabled true
$ docker tag basic-flask-app defaultwesteuacr.azurecr.io/basic-flask-app:latest
$ docker push defaultwesteuacr.azurecr.io/flask-app:latest
```

## Endpoints

[/api/v1/healthcheck](localhost:5000/api/v1/healthcheck)
