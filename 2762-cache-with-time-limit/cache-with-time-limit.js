var TimeLimitedCache = function() {
    this.cache = new Map();
    return 
};

/** 
 * @param {number} key
 * @param {number} value
 * @param {number} duration time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function(key, value, duration) {
    const hadKey = this.cache.has(key)
    this.cache.set(key, [value, duration + Date.now()])
    return hadKey;
};

/** 
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function(key) {
    if (!this.cache.has(key)) {
        return -1;
    }
    const currTime = Date.now();
    const value = this.cache.get(key)[0]
    const duration = this.cache.get(key)[1] 

    if (currTime <= duration) {
        return value
    }

    this.cache.delete(key);
    return -1;
};

/** 
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function() {
    let ans = 0;
    const currTime = Date.now();
    console.log(this.cache.values())
    this.cache.values().forEach((key) => {
        if (currTime <= key[1]) {
            ans += 1
        }
    })
    return ans;
};

/**
 * const timeLimitedCache = new TimeLimitedCache()
 * timeLimitedCache.set(1, 42, 1000); // false
 * timeLimitedCache.get(1) // 42
 * timeLimitedCache.count() // 1
 */