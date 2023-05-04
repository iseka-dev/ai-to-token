var types = require("dis-isa");
var isMatch = require("./isMatch");

/**
 * Returns an array with all the items for which the predicate function returns true for. Or in the
 * case when the predicate is not a function, isMatch is called with predicate as the matching criteria.
 *
 * Predicate functions are called with item, index, and original collection.
 *
 * @param { object | array } input - Collection of items to search in.
 * @param { object | array | string | number | function } predicate - When the predicate is a function
 *  then that is called. Otherwise, isMatch is used to deeply match object structures. The result is a
 *  collection of all the items the predicate returns true for.
 *
 * @returns { array } Collection of items that matched the criteria
 */
function findAll(input, predicate) {
  var result = [];
  var cb = types.isFunction(predicate) ?
    predicate :
    isMatch.withCriteria(predicate);

  for (var item in input) {
    if (input.hasOwnProperty(item) && cb(input[item], item, input)) {
      result.push(input[item]);
    }
  }

  return result;
}

module.exports = findAll;
