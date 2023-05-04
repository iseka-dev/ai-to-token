var types = require("dis-isa");
var arrayToObject = require("./arrayToObject");

/**
 * Pulls out all the items in the input that are **not** in `keys` and returns a new object
 * with just that.
 *
 * @param { object } input - Object to extract data from
 * @param { string | string[] | object } keys - Keys for the values to extract from the input
 *
 * @returns { object } Object with key value pairs of extracted data.
 */
function omit(input, keys) {
  if (!types.isPlainObject(input)) {
    return {};
  }

  if (!types.isArray(keys) && !types.isPlainObject(keys)) {
    keys = [keys];
  }

  if (types.isArray(keys)) {
    keys = arrayToObject(keys);
  }

  return Object
    .keys(input)
    .filter(function(key) {
      return !keys.hasOwnProperty(key);
    })
    .reduce(function(output, item) {
      output[item] = input[item];
      return output;
    }, {});
}

module.exports = omit;
