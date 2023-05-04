var types = require("dis-isa");
var isMatch = require("./isMatch");

/**
 * Find the first item in the input for which the predicate function returns true for. When the
 * predicate is not a function, isMatch is called with the predicate as the matching criteria.
 *
 * Predicate functions are called with item, index, and original collection.
 *
 * @param { object | array } input - Collection of items to search in.
 * @param { object | array | string | number | function } predicate - When the predicate is a
 *  function then that is called. Otherwise, isMatch is used to deeply match object structures.
 *  The result is the first item the predicate returns true for.
 *
 * @returns { Object } First object that matches the provided criteria
 */
function find(input, predicate) {
  var cb = types.isFunction(predicate) ?
    predicate :
    isMatch.withCriteria(predicate);

  for (var item in input) {
    if (input.hasOwnProperty(item) && cb(input[item], item, input)) {
      return input[item];
    }
  }
}

module.exports = find;
