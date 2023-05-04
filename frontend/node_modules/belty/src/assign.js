/**
 * Shallow copies all properties from the input objects (sources) into the target
 * object. Source objects are processed left to right overriding whatever values
 * already exist in the resulting.
 *
 * @param {object} target - Object to copy properties to
 * @param {...} source - The source objects to be merged into the target object
 *
 * @returns {object} Object with all source objects merged in.
 */
function assign(target) {
  var sources = Array.prototype.slice.call(arguments, 1);
  var transform = sources.length > 1 && typeof sources[sources.length - 1] === "function" ? sources.pop() : identity;
  var source, length, i;
  target = target || {};

  // Allow n params to be passed in to extend this object
  for (i = 0, length  = sources.length; i < length; i++) {
    source = sources[i];
    for (var property in source) {
      if (source.hasOwnProperty(property)) {
        target[property] = transform(target[property], source[property]);
      }
    }
  }

  return target;
}

function identity(t, s) {
  return s;
}

module.exports = assign;
