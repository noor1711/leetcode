/**
 * @param {Array} arr
 * @return {Generator}
 */
var inorderTraversal = function*(arr) {
    let inOrder = [];

    function recurse(curr) {
        if (typeof curr === 'number') {
            inOrder.push(curr)
        } 

        if (Array.isArray(curr)) {
            curr.forEach((ele) => recurse(ele))
        }
    }

    recurse(arr);
    for(let a in inOrder) {
        yield Number(inOrder[a]);
    }
};


  const gen = inorderTraversal([1, [2, 3]]);
  gen.next().value; // 1
  gen.next().value; // 2
  gen.next().value; // 3
