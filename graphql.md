# Axios

```
    async function get() {
      const res = await axios.request({
        method: "POST",
        url: "http://localhost:4000",
        data: {
          query: `
          query{
            station(id: "467550") {
              id
              rainfalls {
                date
                value
              }
            }
          }`
        }
      });
      console.log(res);
    }
```
