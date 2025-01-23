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