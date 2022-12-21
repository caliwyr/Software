# Http Response

https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/WWW-Authenticate

## Header

`WWW-Authenticate`

The HTTP WWW-Authenticate response header defines the authentication method that should be used to gain access to a resource.

The WWW-Authenticate header is sent along with a 401 Unauthorized response.

- To prevent browser popup auth dialog

https://forums.couchbase.com/t/best-practice-for-avoiding-browser-401-auth-popup-prompt/11771

https://stackoverflow.com/questions/86105/how-can-i-suppress-the-browsers-authentication-dialog

I encountered the same issue here, and the backend engineer at my company implemented a behavior that is apparently considered a good practice : when a call to a URL returns a 401, if the client has set the header `X-Requested-With: XMLHttpRequest`, the server drops the www-authenticate header in its response.
