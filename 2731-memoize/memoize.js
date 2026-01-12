/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    if (!this.cache) {
        this.cache = new Map()
    }

    this.cache.set(fn, new Map())
    return function(...args) {
        const key = JSON.stringify(args)
        if (!this.cache.get(fn).has(key)) {
            this.cache.get(fn).set(key, fn.apply(this, args))
            
        }
        return this.cache.get(fn).get(key);
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */