# [redis-cli](https://redis.io/topics/rediscli)

```
brew install redis
```

## Connect

```
redis-cli -h localhost -p 6379 ping
```

## Create

`set station-123:2019-02-01 "2.3"`

## Read

- [KEYS](https://redis.io/commands/keys)

`KEYS *`

`get station-123:2019-02-01 // 2.3`

## Update

## Delete
