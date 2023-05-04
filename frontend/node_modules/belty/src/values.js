var types = require("dis-isa");

/**
 * Gets the values from a map and returns them in an array. If an array is passed in, then the array is returned as is.
 *
 * @param {object | Array} input - Input to get values from
 *
 * @returns { Array } - Array of all the values extracted from the input object, or
 *  the array itself if the input is an array.
 */
function values(input) {
  if (types.isArray(input)) {
    return input;
  }

  return Object
    .keys(input)
    .filter(function(key) {
      return input.hasOwnProperty(key);
    })
    .map(function(key) {
      return input[key];
    });
}

module.exports = values;
