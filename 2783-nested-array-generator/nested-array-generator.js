/**
 * @param {Array} curr
 * @return {Generator}
 */
var inorderTraversal = function*(curr) {
    for (let element of curr) {
        if (Array.isArray(element)) {
            yield* inorderTraversal(element)
        } else {
            yield Number(element);
        }
    }
};


  const gen = inorderTraversal([1, [2, 3]]);
  gen.next().value; // 1
  gen.next().value; // 2
  gen.next().value; // 3
