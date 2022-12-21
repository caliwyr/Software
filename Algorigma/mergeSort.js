function mergeSort(nums) {
  if (nums.length === 1) return nums;
  if (nums.length === 2) return nums[0] < nums[1] ? nums : nums.reverse();
  const [nums1, nums2] = divide(nums);
  const sortedNums = merge(mergeSort(nums1), mergeSort(nums2));
  return sortedNums;
}

function divide(nums) {
  const nums1 = nums.slice(0, nums.length / 2);
  const nums2 = nums.slice(nums.length / 2);
  return [nums1, nums2];
}

function merge(nums1, nums2) {
  const mergedNums = [];
  while (nums1.length !== 0 && nums2.length !== 0) {
    mergedNums.push(nums1[0] < nums2[0] ? nums1.shift() : nums2.shift());
  }
  return mergedNums.concat(nums1, nums2);
}

console.log(mergeSort([4, 3, 2, 1, 7, 9, 6, 0]));
