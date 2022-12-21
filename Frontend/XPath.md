# XPath

## Cheat Sheet

https://devhints.io/xpath

##

```js
function getElementByXpath(path) {
  return document.evaluate(
    path,
    document,
    null,
    XPathResult.FIRST_ORDERED_NODE_TYPE,
    null
  ).singleNodeValue;
}

console.log(getElementByXpath("//html[1]/body[1]/div[1]"));
```

## Example

```js
await page.$x(
  `//*[@id="ContentPlaceHolder1_rblNode"]//label[text()="${node.name}"]`
);
```

```js
document
  .evaluate(
    '//label[text()="桃山"]',
    document,
    null,
    XPathResult.ANY_TYPE,
    null
  )
  .iterateNext();
```

```js
document
  .evaluate(
    '//input[@value="檢查格式"]',
    document,
    null,
    XPathResult.ANY_TYPE,
    null
  )
  .iterateNext();
```
