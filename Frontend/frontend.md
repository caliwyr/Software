# i18n

- [Crowdin](https://crowdin.com/)

# Email

## Generator

- [MJMI](https://mjml.io/)

## SAAS

- [Litmus](http://litmus.com/)
- [Sendgrid](https://sendgrid.com/)

## plain text email

https://litmus.com/blog/best-practices-for-plain-text-emails-a-look-at-why-theyre-important

# Error Tracking

- [Sentry](https://sentry.io/welcome/)
- [Honeybadger](https://www.honeybadger.io/)

# Performance

## Optimize Images

- https://developers.google.com/speed/docs/insights/OptimizeImages

- [ImageMagick]()
  For example, you can use convert binary to optimize your JPEG images with the following command (parameters inside brackets are optional):

`convert INPUT.jpg -sampling-factor 4:2:0 -strip [-resize WxH] [-quality N] [-interlace JPEG] [-colorspace Gray/sRGB] OUTPUT.jpg`

- [sharp](https://github.com/lovell/sharp)

# Animation

## parallax scroll

- `background-attachment: fixed;` // not works yet on ios
- [jarallax](https://github.com/nk-o/jarallax)

## scroll reveal

- [scrollreveal](https://github.com/jlmakes/scrollreveal)

# Basic

### Frontend Library

- [react](https://github.com/facebook/react)

### CSS

### Styleguide Library

- [Storybook](https://storybook.js.org/)
- [react-styleguidist](https://github.com/styleguidist/react-styleguidist)
- [Catalog](https://catalog.style)

### Drive user focus

- [Driver.js](http://kamranahmed.info/driver)

### Animation

- [popmotion](https://popmotion.io/)
- [react-motion](https://github.com/chenglou/react-motion)

### Lazy-Loading

- [react-lazyload](https://github.com/jasonslyvia/react-lazyload)

### i18n

- [i18next](https://github.com/i18next/i18next)
- [react-i18next](https://github.com/i18next/react-i18next)
- language tags
  - [wiki](https://en.wikipedia.org/wiki/Language_localisation): There are multiple language tag systems available for language codification. For example, the International Organization for Standardization (ISO) specifies both two- and three-letter codes to represent languages in standards ISO 639-1 and ISO 639-2, respectively.

#### Country Code

- [ISO](https://www.iso.org/obp/ui/#search/code/)
- [ISO-3166-1](https://en.wikipedia.org/wiki/ISO_3166-1) country codes
- [Emoji flag symbols](https://apps.timwhitlock.info/emoji/tables/iso3166)
- [flag-icon-css](https://github.com/lipis/flag-icon-css)

### SEO

- [fetch and render in google webmaster tools not working](https://github.com/prerender/prerender/issues/120#issuecomment-305216710)
  The crawlers do access the `_escaped_fragment_` URLs, but Fetch as Google has a bug where they don't. So you have to manually enter the `?_escaped_fragment_=` query parameter when using Fetch as Google, but the normal Googlebot does not have that issue.

### Networking

#### HTTP

- xhr
- Content-Type
  - MIME type
    - Multipurpose Internet Mail Extensions (MIME) type
      - type/subtype
      - case-insensitive but traditionally is written all in lower case
      - Discrete types
      - Multipart types

#### CORS

- XMLHttpRequest
  - withCredentials: for enabling cookie setting

## Testing

### Framework

- mocha
- jest

### Assertion Library

- Chai

### mocking framework

- Sinon

### Redux

#### Actions Creator

- The most painful point: need to write tons of actions manually! So try some lib to auto-generate those.
- redux-actions: not that usefult
- [redux-saga-routines](https://github.com/afitiskin/redux-saga-routines)
-

#### Async / Side Effect Handler

- redux-thunk: basic and simple one
- [redux-saga](https://github.com/redux-saga/redux-saga): easy to write test

## Form

### Design Pattern

- Leverage html form
- Make sure to do e.preventDefault() while using onSubmit of form in SPA
- Leverage a visibility hidden button for click to submit feature
- Better to have self-hosted state (two ways data binding?)
- Better to have self-hosted validation (base on self-hosted state)
- Better to have field-based composable form structure
- Better to leverage `autofocus` of the first input
- Better to auto open the options while the select is focused

### Modal Form

- Autofocus
- Would be a bit tricky while the form is in the modal (the dom may not be rendered?)
- Make sure to destory the DOM of the form so that autofocus works every time the modal is toggled

### Input

[text-mask](https://github.com/text-mask/text-mask)

## Keyboard Shortcut

### Why Keyboard Shortcut

- Convenient for desktop device
- Useless for mobile and laptop device

### Design Pattern

- Make sure to disable shortcut while input is in focus.
- Better to have a tooltip for hint, or to have a dedicated shortcut page, section, etc.

# React

## HOC, Higher Order Component

### Decorator

babel 6

```sh
yarn add babel-plugin-transform-decorators-legacy

// .babelrc
{
  "plugins": ["transform-decorators-legacy"]
}
```

```js
@withRouter
@connect()
class ComponentWithHOC extend React.Component {}
```

# Headroom

[headroom.js](https://github.com/WickyNilliams/headroom.js)
