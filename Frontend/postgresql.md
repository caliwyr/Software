# Postgresql

## Mac

### Install

```
asdf plugin-add postgres
asdf list all postgres
asdf install postgres 11.10
asdf global postgres 11.10

```

### Stop / Start / Restart

Run this command to manually start the server:
`pg_ctl -D /usr/local/var/postgres -l /usr/local/var/postgres/server.log start`

Start manually:

`pg_ctl -D /usr/local/var/postgres start`

Stop manually:

`pg_ctl -D /usr/local/var/postgres stop` or `brew services stop postgresql`

### Check the listen_addresses and port in postgresql.conf:

`egrep 'listen|port' /usr/local/var/postgres/postgresql.conf`

```
#listen_addresses = 'localhost'         # what IP address(es) to listen on;
#port = 5432                            # (change requires restart)
                                        # supported by the operating system:
                                        # supported by the operating system:
                                        #   %r = remote host and port
```

### Bug

- DB can't be connectted after Mac restart

```
psql: could not connect to server: No such file or directory
Is the server running locally and accepting
connections on Unix domain socket "/tmp/.s.PGSQL.5432"?
```

[The problem can also be attributed to a crashed process that left postmaster.pid file behind.](https://dba.stackexchange.com/a/171580)

```
$ brew services stop postgresql
$ rm /usr/local/var/postgres/postmaster.pid # adjust path accordingly to your install
$ brew services start postgresql
```

# Migration

- [db-migrate](https://github.com/db-migrate/node-db-migrate)
- [node-pg-migrate](https://github.com/salsita/node-pg-migrate)
- [sqitch](https://github.com/sqitchers/sqitch)

# User

https://www.liquidweb.com/kb/what-is-the-default-password-for-postgresql/

```
psql
// psql: FATAL: role "root" does not exist

su - postgres
psql
```

When connecting to PostgreSQL on Linux for the first time many admins have questions, especially if those admins are from the MySQL world. By default, when PostgreSQL is installed, a `postgres` user is also added.

The first question many ask is, “What is the default password for the user postgres?” The answer is easy… there isn’t a default password. The default authentication mode for PostgreSQL is set to ident.

## Create user

```
createuser
```

# Drop database

```
REVOKE CONNECT ON DATABASE dbname FROM PUBLIC, username;

// If PostgreSQL < 9.2
SELECT pg_terminate_backend(procpid) FROM pg_stat_activity WHERE datname = 'mydb';
// Else
SELECT pg_terminate_backend(pid) FROM pg_stat_activity WHERE datname = 'mydb';
```

https://tableplus.io/blog/2018/04/postgresql-how-to-drop-database-with-active-connections.html

# Connection

List connection

```
SELECT * FROM pg_stat_activity;
```
