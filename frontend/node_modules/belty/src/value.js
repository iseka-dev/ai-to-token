var identity = require("./identity");
var splitKeypath = require("split-keypath");
var types = require("dis-isa");

/**
 * Extract the value from an input object for the given keypath.
 *
 * @param {object} input - Object to read `property` from.
 * @param {string|number|array} keypath - keypath for the value in the object.
 * @param {function?} transform -  Function that is called to transform the result.
 *  The function is called with the result, keypath and the input. The result from
 *  calling the transform is returned.
 *
 * @returns {*} The value for the corresponding keypath.
 */
function value(input, keypath, transform) {
  if (!keypath) {
    return;
  }

  if (types.isString(keypath)) {
    keypath = splitKeypath(keypath);
  }
  else if (!types.isArray(keypath)) {
    keypath = [keypath];
  }

  // Find value...
  var value = keypath.reduce(function(nested, key) {
    return nested[key];
  }, input);

  return (transform || identity)(value, keypath, input);
}

module.exports = value;
