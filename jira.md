next release filter

```
assignee = yes AND project = CORE AND fixVersion in ("2019-08-20", EMPTY) OR
```

``` deprecated
assignee = yes AND project = "EMQ Connect Management" AND (status not in (NEW, CLOSED) OR status = CLOSED AND updatedDate > 2019-08-20) OR 
assignee = yes AND project = "Mobile Team" AND (fixVersion = 2019-08-20 OR fixVersion = EMPTY AND status not in (New, DONE)) OR
assignee = yes AND project = "Web Development" AND (status not in ("To Do", DONE) OR status = DONE AND updatedDate > 2019-08-20)
```