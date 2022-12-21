# Mac (Deprecated)

```
brew install postgresql
brew list

psql --version

ps auxwww | grep postgres
```

https://stackoverflow.com/a/7975660/1860639

The Homebrew package manager includes launchctl plists to start automatically. For more information run brew info postgres.

Start manually:

```
pg_ctl -D /usr/local/var/postgres start
```

Stop manually:

```
pg_ctl -D /usr/local/var/postgres stop
```

Start automatically:

"To have launchd start postgresql now and restart at login:"

```
brew services start postgresql
```

https://www.postgresql.org/docs/9.2/static/app-psql.html
https://gist.github.com/Kartones/dd3ff5ec5ea238d4c546
http://postgresguide.com/utilities/psql.html

`\dt *.*`: List tables from all schemas (if _._ is omitted will only show SEARCH_PATH ones)

# Docker

# Start a postgresql

```sh
docker run --rm --name pg-docker -e POSTGRES_PASSWORD=docker -d -p 5432:5432 postgres
docker run \
--rm \
--name pg-docker \
-e POSTGRES_PASSWORD=docker
-d \
-p 5432:5432 \
-v $HOME/docker/volumes/postgres:/var/lib/postgresql/data \
postgres
```

- `--rm`: Automatically remove the container and it’s associated file system upon exit. In general, if we are running lots of short term containers, it is good practice to to pass rm flag to the docker run command for automatic cleanup and avoid disk space issues. We can always use the v option (described below) to persist data beyond the lifecycle of a container
- `--name`: An identifying name for the container. We can choose any name we want. Note that two existing (even if they are stopped) containers cannot have the same name. In order to re-use a name, you would either need pass the rm flag to the docker run command or explicitly remove the container by using the command docker rm [container name].
- `-e`: Expose environment variable of name POSTGRES_PASSWORD with value docker to the container. This environment variable sets the superuser password for PostgreSQL. We can set POSTGRES_PASSWORD to anything we like. I just choose it to be docker for demonstration. There are additional environment variables you can set. These include POSTGRES_USER and POSTGRES_DB. POSTGRES_USER sets the superuser name. If not provided, the superuser name defaults to postgres. POSTGRES_DB sets the name of the default database to setup. If not provided, it defaults to the value of POSTGRES_USER.
- `-d`: Launches the container in detached mode or in other words, in the background.
- `-p`: Bind port 5432 on localhost to port 5432 within the container. This option enables applications running out side of the container to be able to connect to the Postgres server running inside the container.
- `-v`: Mount \$HOME/docker/volumes/postgres on the host machine to the container side volume path /var/lib/postgresql/data created inside the container. This ensures that postgres data persists even after the container is removed.

[Don’t install Postgres. Docker pull Postgres](https://hackernoon.com/dont-install-postgres-docker-pull-postgres-bee20e200198)

# Connect postgresql

```
psql -h localhost -U postgres -d postgres
```

# IDE

[Postico](https://eggerapps.at/postico/)

# Meta-Commands

https://www.postgresql.org/docs/9.2/app-psql.html

\l (or \list)
\l+ (or \list+)
List the names, owners, character set encodings, and access privileges of all the databases in the server. If + is appended to the command name, database sizes, default tablespaces, and descriptions are also displayed. (Size information is only available for databases that the current user can connect to.)

\q or \quit
Quits the psql program. In a script file, only execution of that script is terminated.

# Command

`\dt`: list tables

`\l`: list databases

`\du`: list users

# Run SQL Query

```
psql -U yes -d yes-db -c 'Select * from yes-table'
```

## Pretty

```
\x on
```