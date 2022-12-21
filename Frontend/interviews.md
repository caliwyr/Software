- https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise
- https://eddmann.com/posts/implementing-promise-all-and-promise-race-in-javascript/

# Implementing Promise.all

```
const all = (...promises) => {
    const results = [];
    for(const [i, promise] of promises.entries()){
        promise.then(res => {
            results[i] = res
        }).catch(()=>{
            return new Promise().reject()
        })
    }
    return new Promise().resolve(results)
}
```

test

```
var p1 = Promise.resolve(3);
var p2 = 1337;
var p3 = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve("foo");
  }, 100);
});

Promise.all([p1, p2, p3]).then(values => {
  console.log(values); // [3, 1337, "foo"]
});
```

# Implementing Promise.race

# Implementing connect of React-Redux

- https://github.com/reduxjs/react-redux/blob/master/src/connect/connect.js
- https://blog.jakoblind.no/learn-react-redux-by-coding-the-connect-function-yourself/

```
const connect = (props) => (options) => (WrappedComponent) => {
    store.update()
    return <WrappedComponent {...props} />
}
```
