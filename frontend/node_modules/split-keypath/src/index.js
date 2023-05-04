/**
 * Method that converts a string of object and array keys, which we also
 * refer to as keypath, to an array of keys that can be used for reading
 * nested values in an object.
 */
function splitKeypath(input) {
  var regex = /(\w+)|\[([^\]]+)\]/g;
  var result = [];
  var path;

  while ((path = regex.exec(input || ''))) {
    if (input[path.index] === '[') {
      result.push(path[2]);
    }
    else {
      result.push(path[1]);
    }
  }

  return result;
}

module.exports = splitKeypath;
