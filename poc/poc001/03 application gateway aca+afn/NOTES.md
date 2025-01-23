# NOTES

## Target

The target is to deploy the Container App and Azure Function to one shared domain, divided by a service prefix (aca, afn)

https://basic-azure-function.azurewebsites.net/api/http_trigger?code=*
=>
http://4.175.28.248/afn/api/http_trigger?code=*
=>
poc03.enricogoerlitz.com//api/http_trigger?code=*

----

https://basic-flask-app.jollysmoke-5a66fa20.westeurope.azurecontainerapps.io/aca/api/v1/*
=>
http://4.175.28.248/aca/api/v1/*
=>
poc03.enricogoerlitz.com/aca/api/v1/*

## Application Gateway config

- no backend pools
- backend-settings: https + all default
- listeners: http
- rules:
    - Redirection > external site | ggf with or without path
    - two path rules: /afn/\*, /aca/\* > with Redirection