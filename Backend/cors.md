# CORS

https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS

Cross-Origin Resource Sharing (CORS) is a mechanism that uses additional HTTP headers to tell browsers to give a web application running at one origin, access to selected resources from a different origin. A web application executes a cross-origin HTTP request when it requests a resource that has a different origin (domain, protocol, or port) from its own.

## How to enable CORS?

Expressjs

```
app.use(cors);
```

## Step by step

The Cross-Origin Resource Sharing standard works by adding new HTTP headers that let servers describe which origins are permitted to read that information from a web browser.

http response must have headers:

- Access-Control-Allow-Origin
- Access-Control-Expose-Headers
- Access-Control-Max-Age
- Access-Control-Allow-Credentials
- Access-Control-Allow-Methods
- Access-Control-Allow-Headers

!!Important

## Common issue

- Client forgets to add `withCredentials = true`!!

- Credentials mode is include, so that `Access-Control-Allow-Origin` can't be `*`.

Response to preflight request doesn't pass access control check: The value of the 'Access-Control-Allow-Origin' header in the response must not be the wildcard '\*' when the request's credentials mode is 'include'. The credentials mode of requests initiated by the XMLHttpRequest is controlled by the withCredentials attribute.

- It does not have HTTP ok status.
  https://stackoverflow.com/questions/57640113/cors-it-does-not-have-http-ok-status

You may need to enable pre-flight requests for your route

```
app.use(cors())

app.options('/post/login', cors()) // enable pre-flight requests
app.post('/post/login', (req, res, next) => {
// your code here
});
or for all routes

app.options('\*', cors())
```
