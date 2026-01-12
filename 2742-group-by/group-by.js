/**
 * @param {Function} fn
 * @return {Object}
 */
Array.prototype.groupBy = function(fn) {
        const arr = this;
        let response = {};

        for(let element of arr) {
            const key = fn(element);

            if (!(key in response)) {
                response[key] = []
            }

            response[key].push(element)
        }
        
        return response;
    
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */