# PWA, Progressive Web App

## [Add to Home Screen (web app install prompt)](https://developers.google.com/web/fundamentals/app-install-banners/)

Criterias:

- The web app is not already installed.
  - and prefer_related_applications is not true.
- Meets a user engagement heuristic (currently, the user has interacted with the domain for at least 30 seconds)
- Includes a web app manifest that includes:
  - short_name or name
  - icons must include a 192px and a 512px sized icons
  - start_url
  - display must be one of: fullscreen, standalone, or minimal-ui
- Served over HTTPS (required for service workers)
- Has registered a service worker with a fetch event handler
