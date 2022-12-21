[cron cheatsheet](https://devhints.io/cron)
[The Ultimate Crontab Cheatsheet](https://www.codementor.io/akul08/the-ultimate-crontab-cheatsheet-5op0f7o4r)

# Format

Min Hour Day Mon Weekday

```
* * * * * command to be executed
┬ ┬ ┬ ┬ ┬
│ │ │ │ └─ Weekday (0=Sun .. 6=Sat)
│ │ │ └────── Month (1..12)
│ │ └─────────── Day (1..31)
│ └──────────────── Hour (0..23)
└───────────────────── Minute (0..59)
```

# Crontab

```sh
# Adding tasks easily
echo "@reboot echo hi" | crontab
# Open in editor
crontab -e
# List tasks
crontab -l [-u user]
```

- -e (edit user's crontab)
- -l (list user's crontab)
- -r (delete user's crontab)
- -i (prompt before deleting user's crontab)

```sh
crontab -e
* * * * * cd ~/app/pangolin && /usr/local/bin/docker-compose run -d --no-deps crawler node src/getStation.js
```

```sh
crontab -l
```

# Log

```sh
sudo grep CRON /var/log/syslog*
sudo grep CRON /var/log/syslog* | grep -E "(yes)"
```
