# Flask demo app

## Build docker

```bash
 docker build  -t narenm/flask .
```

## Run docker image

```bash
docker run -it  -v $PWD:/webapp -p 80:80 -p 5000:5000 narenm/flask
```