/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = function(functions) {
    let results = [];
    let completed = 0;

    return new Promise((resolve, reject) => {

    
        functions.forEach(async(fn, index) => {
                
                try {
                    const result = await Promise.resolve(fn.apply(this));
                
                    results[index] = result;
                    completed += 1

                    if (completed === functions.length) {
                        resolve(results)
                    }
                } catch (err) {
                    reject(err)
                }
            }
            )
            
        });
};

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */