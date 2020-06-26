# Demo ImportError: undefined symbol: PQencryptPasswordConn

Build the docker image:

```shell
docker build -t psycopg2/buildozer .
```

Run image interactively and attach usb for deployment:
```shell
docker run --rm -v "$(pwd)":/home/user/hostcwd -v /dev/bus/usb:/dev/bus/usb --privileged -it --entrypoint=bash psycopg2/buildozer 
```

Interact with buildozer as usual, to build:
```shell
buildozer android debug
```

To deploy and run on target
```shell
buildozer android deploy run
```

For debugging, the log is pretty huge and includes more than just this application, it's best to throw it in a file and analyze it after the app crashed.
```shell
buildozer android deploy run logcat > out.log
```
