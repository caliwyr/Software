# Reduce size by CDN

https://medium.com/comparethemarket/how-to-reduce-your-bundle-size-by-automatically-getting-your-dependencies-from-a-cdn-96b25d1e228

- [dynamic-cdn-webpack-plugin](https://github.com/mastilver/dynamic-cdn-webpack-plugin)
- [unpak](https://unpkg.com/)
- [externals](https://webpack.js.org/configuration/externals/)

```js
new DynamicCdnWebpackPlugin({
  env: "production",
  only: [
    "react",
    "react-dom",
    "lodash",
    "leaflet",
    "d3",
    "formik",
    "react-router",
    "react-router-dom",
  ],
}),
```
