var types = require("dis-isa");

/**
 * Method that extracts key value pairs from the input object and returns that in a new object
 * in a new shallow copy of the input object.
 *
 * @param { object } input - Object to extract data from
 * @param { string | string[] | object } keys - Keys for the values to extract from the input
 *
 * @returns { object } Object with key value pairs of extracted data.
 */
function pick(input, keys) {
  if (!types.isPlainObject(input)) {
    return {};
  }

  if (!types.isArray(keys) && !types.isPlainObject(keys)) {
    keys = [keys];
  }
  else if (types.isPlainObject(keys)) {
    keys = Object.keys(keys);
  }

  return keys
    .filter(function(key) {
      return input.hasOwnProperty(key);
    })
    .reduce(function(output, item) {
      output[item] = input[item];
      return output;
    }, {});
}

module.exports = pick;
