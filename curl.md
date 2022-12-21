- [Everything curl](https://ec.haxx.se/)

# Get Request Time

```
-w %{time_connect}:%{time_starttransfer}:%{time_total}
```

# Get

```
curl http://localhost:3000/users
```

# Post

```
curl \
  -i \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"username":"yes","password":"yes"}' \
  http://localhost:3000/signup
```

- [`--data, -d`](<(https://curl.haxx.se/docs/manpage.html#-d)>): Sends the specified data in a POST request to the HTTP server.
- --include, -i: All HTTP replies contain a set of response headers that are normally hidden, use curl's --include (-i) option to display them as well as the rest of the document.
- --request, -X : Change the method keyword curl selects.

## Get cookie from response

TBD

response.headers["set-cookie"]

# Wait until localhost post open

https://stackoverflow.com/questions/11904772/how-to-create-a-loop-in-bash-that-is-waiting-for-a-webserver-to-respond

```
until $(curl --output /dev/null --silent --head --fail http://myhost:myport); do
    printf '.'
    sleep 5
done
```

- [--output](https://curl.haxx.se/docs/manpage.html#-o): Write output to <file> instead of stdout.
- [--silent](https://curl.haxx.se/docs/manpage.html#-s): Silent or quiet mode. Don't show progress meter or error messages.
- [--head](https://curl.haxx.se/docs/manpage.html#-I): (HTTP FTP FILE) Fetch the headers only!
- [--fail](https://curl.haxx.se/docs/manpage.html#-f): (HTTP) Fail silently (no output at all) on server errors.
