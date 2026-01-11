/**
 * @param {Array} arr
 * @param {number} depth
 * @return {Array}
 */
var flat = function (arr, n) {
    

    function flatten(ele, depth) {
        const curr = ele;
        let ans = [];
        if (curr?.hasOwnProperty("length") && depth <= n) {
            curr.forEach((element) => ans.push(...flatten(element, depth + 1)))
        } else {
            ans.push(ele)
        }

        return ans
    }

    return flatten(arr, 0)

};