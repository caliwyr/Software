# Backup

Dump

[pg_dump](https://www.postgresql.org/docs/current/app-pgdump.html)

Output

- Script dumps
  - plain-text files containing the SQL commands
  - To restore from such a script, feed it to psql.
- Archive file formats
  - must be used with pg_restore to rebuild the database

Restore

## Example

```
// db-backup.sh
#!/bin/sh
docker-compose exec db pg_dump -U yes -d pangolin >./db/backup/db-backup-$(date +%Y%m%d%H%M%S).sql
```

```
// db-restore.sh
cat db-backup.sql | docker-compose exec db psql -U yes -d pangolin 
```
