# Interpret Contents of a Dockerfile

Always called `Dockerfile`
Works like a shell script

## Components

Specify the base docker image to pull down (in this case Ubuntu 18.04)

```
FROM ubuntu:18.04
```

Specify the name of the maintainer (optional)

```
MAINTAINER Sample Maintainer (samplemaintainer@coolcoders.biz)
```

Run known applications within the new container

```
RUN apt update && apt install -y python3-pip python3-dev
```

Run raw shell commands within the container

```
CMD ["ufw allow 5000"]
```

Copy a local file to the container

```
COPY ./requirements.txt /app/requirements.txt
```

Change working directory

```
WORKDIR /app
```

Specity the program to run on container startup followed by the parameters

```
ENTRYPOINT ["python3"]
CMD ["myAPI.py"]
```
