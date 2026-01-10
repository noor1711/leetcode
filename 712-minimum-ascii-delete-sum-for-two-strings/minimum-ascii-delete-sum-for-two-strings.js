/**
 * @param {string} s1
 * @param {string} s2
 * @return {number}
 */

function findStringSum(s) {
    return s.split("").reduce((total, ch) => total + ch.charCodeAt(), 0)
}

var minimumDeleteSum = function(s1, s2) {
    const m = s1?.length
    const n = s2?.length
    const dic = new Map()

    const recurse = (index1, index2) => {
        const key = index1 + "," + index2
        if (dic.has(key)) {
            return dic.get(key);
        }

        if (index1 == m) {
            return findStringSum(s2.slice(index2))
        } else if (index2 == n) {
            return findStringSum(s1.slice(index1))
        }

        let one = null;
        if (s1[index1] === s2[index2]) {
            one = recurse(index1 + 1, index2 + 1); 
        }

        let two = Math.min(findStringSum(s1[index1]) + recurse(index1 + 1, index2), findStringSum(s2[index2]) + recurse(index1, index2 + 1))
        dic.set(key, one === null ? two : Math.min(one, two))
        return dic.get(key)
    }

    return recurse(0, 0)
};