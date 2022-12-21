## Plugin

- HTMLWebpackPlugin

- CommonsChunkPlugin

- ExtractTextPlugin

- snippet

```
module.exports = {
  entry: {
  }
}
```

# Config to enable root importing

https://github.com/hiiamyes/cheat-sheet/blob/master/vscode/vscode.md#import-path-base-url

# Analyzer

Official

https://github.com/webpack/analyse

```
webpack --profile --json > stats.json
```

SAAS

- [packtracker](https://packtracker.io)

OSS

- [webpack-visualizer](https://chrisbateman.github.io/webpack-visualizer/)

https://chrisbateman.github.io/webpack-visualizer/

```
webpack --json > stats.json
```

- [webpack-bundle-analyzer](https://github.com/webpack-contrib/webpack-bundle-analyzer)

```
    "webpack:profile": "webpack --profile --json > stats.json",
    "analyze:bundle": "webpack:profile webpack-bundle-analyzer stats.json"
```
