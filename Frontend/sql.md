```
DROP DATABASE db-name;

// ERROR:  cannot drop the currently open database

```

# Upsert

```
insert into stations (station_id, name)
values (
    $1,
    $2
)
on conflict (station_id)
do
update set name = $1;
```

# ON CONFLICT

https://www.postgresql.org/docs/9.5/sql-insert.html#SQL-ON-CONFLICT

```
INSERT INTO distributors (did, dname) VALUES (7, 'Redline GmbH')
ON CONFLICT (did) DO NOTHING;
```
