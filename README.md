### Note: Used python 3.9.9 in this project

- You can use function.zip file on aws lambda


### Aws Deploy - API URL

https://eibb89rszb.execute-api.eu-central-1.amazonaws.com/dev/

**Api Path:** /api/array

### CURL Example

```bash

curl -X POST https://eibb89rszb.execute-api.eu-central-1.amazonaws.com/dev/api/array
   -H 'Content-Type: application/json'
   -d '{"input": [1, [2,3, [4]], [5], 6, [7, [8]]]}'

```
