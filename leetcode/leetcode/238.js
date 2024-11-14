var filter = function(arr, fn) {
    const filteredArr = [] // Initialize an empty array to hold the filtered results.
    // Iterate over each element of the input array 'arr' using forEach.
    // 'item' is the current element of the array, and 'i' is its index.
    arr.forEach(function(item, i){
        // Apply the filtering function 'fn' to the current element.
        // 'fn' is expected to return a truthy value (like true, a non-zero number, etc.)
        // if the element should be included in the filtered array.
        if(fn(arr[i], i)) {
            // If the filtering condition is met (i.e., fn returns true),
            // add the current element 'arr[i]' to the filteredArr array.
            filteredArr.push(arr[i]) 
        }
    })
    return filteredArr // Return the new array containing only the elements that passed the filter.
};