# Font Family & Font Face

- [normalize.css](https://github.com/necolas/normalize.css/issues/665)
- [system font stack](https://css-tricks.com/snippets/css/system-font-stack/)
- [Typography - Atlassian Design](https://atlassian.design/guidelines/product/foundations/typography)
  - use sans-serif fonts for most of our type
  - to display code then you should defer to monospace fonts.

```css
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Roboto",
    "Oxygen", "Ubuntu", "Fira Sans", "Droid Sans", "Helvetica Neue", sans-serif;
}
```

```css
font-family: "SF Mono", "Segoe UI Mono", "Roboto Mono", "Ubuntu Mono", Menlo,
  Courier, monospace;
```

```css
@font-face {
  font-family: myFirstFont;
  src: url(sansation_light.woff);
}
```

# Font Size

https://cnpagency.com/blog/the-mathematical-advantage-of-a-16px-base-font-size/

TL:DR; Start using 16px as your base font and use ems to size everything based off of that, and you'll be a far happier person.

The problem is that 14 isn’t very divisible: its divisible factors are 7 and 2; but 16 is divisible by 8, 4 and 2. What difference does that make? I have a handy table to show the advantage of using 16px as a base font size:

| 10          | 12          | 14   | 16           | 18           | 20           | 22           | 24           |
| ----------- | ----------- | ---- | ------------ | ------------ | ------------ | ------------ | ------------ |
| .625        | .75         | .875 | 1rem         | 1.125        | 1.25         | 1.375        | 1.5          |
| .7142857143 | .8571428571 | 1rem | 1.1428571429 | 1.2857142857 | 1.4285714286 | 1.5714285714 | 1.7142857143 |

- Setup base `font-size` of `<html />`
- Use `rem`:
  - The rem (root em) works in exactly the same way as the em, except that it will always equal the size of the default base font-size.
  - The default base font-size given to web pages by web browsers before CSS styling is applied is 16 pixels.

```css
/* global.css */
html {
  font-size: 16px;
}

button {
  font-size: 1rem;
}
```

# Type Scale

https://material.io/design/typography/the-type-system.html#
https://developer.mozilla.org/en-US/docs/Web/CSS/line-height

| Scale Category | Weight | Size | Letter spacing | Line height  |
| -------------- | ------ | ---- | -------------- | ------------ |
| H1             |        | 96   |                | normal (1.2) |
| H2             |        | 60   |                | normal (1.2) |
| H3             |        | 48   |                | normal (1.2) |
| H4             |        | 34   |                | normal (1.2) |
| H5             |        | 24   |                | 30           |
| H6             |        | 20   |                | normal (1.2) |
