# Google sheet

## Fixed column

=IFS(ROW() = 4, $W$21 - sum($AG$4:AG7), AK6>0, $W$21 - sum($AG$4:AG7), sum($AG$4:AG7) > $W$21, -AG7)

## query

=QUERY(employees!A:D,"select A where C = '"&B2&"'")

arrayformula for query is not supported

## vlookup

=ARRAYFORMULA(VLOOKUP(B3:B,{employees!C2:C, employees!D2:D},2,false))

## lookup

https://support.google.com/docs/answer/3256570?hl=en

```
```

## index

https://support.google.com/docs/answer/3098242?hl=en&ref_topic=3105472

```
=INDEX(A1:E7, MATCH("Course 3", A:A, 0), MATCH("Pablo", 1:1, 0))
```