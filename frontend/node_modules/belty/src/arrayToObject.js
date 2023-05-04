var types = require("dis-isa");

/**
 * Converts arrays to a literal objects with the array values as keys. You can optionally
 * pass in a callback function that is called in order to generate the values that go
 * in the final result. `val` can also just be anything to be used as the value for each
 * entry in the final result, otherwise `true` is used.
 *
 * This method is useful in situation where you need to create a lookup table such as
 * an object map (enums).
 *
 * @param { array } input - Items to convert to a map
 * @param { *? } val - Can be a function, in which case it is called with the currect
 *  item in the array being processed in order to derive the value for the map entry.
 *  Otherwise the value will be the same as the value in the array, which will also
 *  be the key.
 *
 * @returns { object } Object will all the array values as keys and the derived
 *  values
 */
function arrayToObject(input, val) {
  var defaultValue = true;
  if (arguments.length !== 1) {
    if (!types.isFunction(val)) {
      defaultValue = val;
      val = false;
    }
  }

  return input.reduce(function(container, value, key) {
    var _key = value, _value = defaultValue;

    if (val) {
      var result = val(value, key, input);
      if (types.isArray(result)) {
        _key = result[0];
        _value = result[1];
      }
      else {
        _value = result;
      }
    }

    container[_key] = _value;
    return container;
  }, {});
}

module.exports = arrayToObject;
