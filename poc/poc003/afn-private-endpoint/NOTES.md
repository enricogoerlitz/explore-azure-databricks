# NOTES

## Prerequisites

1. Download: [Azure Functions Core Tools](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=macos%2Cisolated-process%2Cnode-v4%2Cpython-v2%2Chttp-trigger%2Ccontainer-apps&pivots=programming-language-python)

```sh
$ brew tap azure/functions
$ brew install azure-functions-core-tools@4
# if upgrading on a machine that has 2.x or 3.x installed:
$ brew link --overwrite azure-functions-core-tools@4
```

2. Install VS-Code extensions

- Azure Functions
- Azure Tools

## Connection settings

**VNET**

- at least 8 IPs for the azure function VNET

**Key Vault**

- RBAC Access Control!
- only selected networks > subnet of azure function outbound VNET integration

**Cosmos-DB**

- NoSQL default
- only selected networks > subnet of azure function outbound VNET integration


**Azure Function**

- Identity > Status=ON; Role=Key Vault Secrets User
- Networking > outbound vnet integration > select allowed subnet
https://www.youtube.com/watch?v=6HKj5hOuD00&ab_channel=MicrosoftAzure
