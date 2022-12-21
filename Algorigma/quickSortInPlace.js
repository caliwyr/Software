function quickSort(nums, left = 0, right = nums.length - 1) {
  if (left < right) {
    const pivotIndex = partition(nums, left, right);
    quickSort(nums, left, pivotIndex - 1);
    quickSort(nums, pivotIndex + 1, right);
  }
}

const partition = (arr, left, right) => {
  const pivot = arr[right];
  let pivotIndex = left;
  for (let i = left; i < right; i++) {
    if (arr[i] < pivot) {
      swap(arr, i, pivotIndex);
      pivotIndex++;
    }
  }
  swap(arr, pivotIndex, right);
  return pivotIndex;
};

const swap = (arr, left, right) => {
  const temp = arr[left];
  arr[left] = arr[right];
  arr[right] = temp;
};

const nums = [4, 3, 2, 1, 7, 9, 6, 0];
quickSort(nums);
console.log(nums);

// [4152]
// pivot=2
// pi=0
// i=0, 4<2
// i=1, 1<2, 1452, pi=1
// i=2, 5<2,
// 2145
