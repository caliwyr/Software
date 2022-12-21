function countingSort(nums) {
  const countArr = [];
  const outputArr = [];
  for (num of nums) {
    countArr[num] = countArr[num] ? countArr[num] + 1 : 1;
  }
  for (let i = 0; i < countArr.length; i++) {
    let count = countArr[i];
    while (count > 0) {
      outputArr.push(i);
      count--;
    }
  }
  return outputArr;
}
console.log(countingSort([4, 4, 4, 3, 2, 2, 2, 1, 7, 9, 6, 0]));
