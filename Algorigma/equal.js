const TreeNode = val => {
  this.val = val;
  this.left = null;
  this.right = null;
};

const equal = (s, t) => {};

const s = new TreeNode(1);
s.left = new TreeNode(2);
s.right = new TreeNode(3);

const t = new TreeNode(1);
t.left = new TreeNode(2);
t.right = new TreeNode(3);

console.log(equal(s, t));
