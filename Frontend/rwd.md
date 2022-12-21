# RWD

- [ua-parser-js](https://github.com/faisalman/ua-parser-js)

# Breakpoints

- [Bootstrap 4](https://getbootstrap.com/docs/4.0/layout/overview/#responsive-breakpoints)

```
// Extra small devices (portrait phones, less than 576px)
// No media query since this is the default in Bootstrap

// Small devices (landscape phones, 576px and up)
@media (min-width: 576px) { ... }

// Medium devices (tablets, 768px and up)
@media (min-width: 768px) { ... }

// Large devices (desktops, 992px and up)
@media (min-width: 992px) { ... }

// Extra large devices (large desktops, 1200px and up)
@media (min-width: 1200px) { ... }
```

```css
@media (min-width: 1200px) .container {
  max-width: 1140px;
}
@media (min-width: 992px) .container {
  max-width: 960px;
}
@media (min-width: 768px) .container {
  max-width: 720px;
}
@media (min-width: 576px) .container {
  max-width: 540px;
}
```
