var types = require("dis-isa");

/**
 * Converts an input to an array if it is not already an array.
 *
 * @param {*} input - Data to convert to an array
 *
 * @returns { Array }
 */
function toArray() {
  var i = 0;
  var input = arguments;
  var length = arguments.length;
  var result = [];

  // Optimization path for cases where there is only one input and
  // it already is an array.
  if (arguments.length === 1 && types.isArray(arguments[0])) {
    return arguments[0];
  }

  while (i < length) {
    if (types.isArray(input[i])) {
      result = result.concat(input[i]);
    }
    else {
      result.push(input[i]);
    }

    i++;
  }

  return result;
}

module.exports = toArray;
