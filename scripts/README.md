## Jenkins containers ## 

These scripts spin up Jenkins master and slave instances as docker containers from [https://hub.docker.com/r/lnarmour/parric/tags/](https://hub.docker.com/r/lnarmour/parric/tags/).

Create **master**:
```
./master.sh
```

Get the secret from the node definition in jenkins master. The slave needs this to connect to master. Create **slave**:
```
./slave.sh <secret>
```
