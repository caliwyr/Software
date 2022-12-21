# Check DNS

`host -t ns {domain.name}`

# Domain Name

## Buy Domain

- [Godaddy](https://tw.godaddy.com)
- [Hover](https://hover.com)

# TLD, Top Level Domain

ICANN: Internet Corporation for Assigned Names and Numbers

https://en.wikipedia.org/wiki/List_of_Internet_top-level_domains
The official list of all top-level domains is maintained by the Internet Assigned Numbers Authority (IANA) at the Root Zone Database.

# Redirect

```js
import React from "react";
import Helmet from "react-helmet";

const Redirect = props => {
  const {
    url
    // pageContext: { url }
  } = props;
  return (
    <Helmet>
      <meta http-equiv="refresh" content={`0;url=${url}`} />
    </Helmet>
  );
};

export default Redirect;
```
