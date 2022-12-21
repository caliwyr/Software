# Time complexity

- Divide and conquer: O(nlogn)

| Algorithm     | Best  | Average | Worst | Memory | Stable | Space | Comments                    |
| ------------- | ----- | ------- | ----- | ------ | ------ | ----- | --------------------------- |
| Quick Sort    | nlogn | nlogn   | ?     | ?      | ?      | 1     |                             |
| Merge Sort    |       |         | ?     | ?      | ?      |       |                             |
| Counting Sort | n+r   | n+r     | n+r   | n+r    | Yes    |       | r - biggest number in array |

# nlogn

- arr.length = n

```
1 + 2 + 4 + 2^3 + ... + 2^(m-1) = n
1*(2^m-1)/(2-1) = n
2^m-1 = n
2^m = n+1
m = log2(n+1)
```
