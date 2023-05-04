const toString = Function.prototype.apply.bind(Object.prototype.toString);

const bufferSignature  = typeof Buffer !== "undefined" ? toString(new Buffer(1)) : "[object Uint8Array]";
const booleanSignature = toString(true);
const regexSignature   = toString(/test/);
const dateSignature    = toString(new Date());
const arraySignature   = toString([]);
const objectSignature  = toString({});
const errorSignature   = toString(new Error());
const numberSignature  = toString(1);


/**
 * Checks if the input is a boolean
 */
function isBoolean(item) {
  return toString(item) === booleanSignature;
}

/**
 * Checks is the input is a number
 */
function isNumber(item) {
  return toString(item) === numberSignature;
}

/**
 * Checks if the input is a Buffer
 */
function isBuffer(item) {
  return toString(item) === bufferSignature;
}

/**
 * Check if input is undefined
 *
 * @param {*} item - Item to be tested for undefined
 * @returns {boolean}
 */
function isUndefined(item) {
  return item === (void 0);
}

/**
 * Check if input is null
 *
 * @param {*} item - Item to be tested for null
 * @returns {boolean}
 */
function isNull(item) {
  return item === null;
}

/**
 * Check if input is a regulat expression
 *
 * @param {*} item - Item to check for regular expression
 * @returns {boolean}
 */
function isRegex(item) {
  return !!item && toString(item) === regexSignature;
}

/**
 * Check if input is an array
 *
 * @param {*} item - Item to be tested for Array
 * @returns {boolean}
 */
const isArray = (function() {
  if (Array.isArray) {
    return Array.isArray;
  }

  return function(item) {
    return toString(item) === arraySignature;
  };
})();

/**
 * Check if input is a function
 *
 * @param {*} item - Item to be tested for function
 * @returns {boolean}
 */
function isFunction(item) {
  return typeof item === "function";
}

/**
 * Check if input is a string
 *
 * @param {*} item - Item to check for string
 * @returns {boolean}
 */
function isString(item) {
  return typeof item === "string";
}

/**
 * Check if input is an object. Objects are:
 *  - literal object, object instances, arrays, null
 *
 * @param {*} item - Item to check for object
 * @returns {boolean}
 */
function isObject(item) {
  return typeof item === "object";
}

/**
 * Check if input is a Date
 *
 * @param {*} item - Item to be tested for Date
 * @returns {boolean}
 */
function isDate(item) {
  return toString(item) === dateSignature;
}

/**
 * Check if item is an object literal - plain object.
 * A plain object is an object without prototype, or a prototype equals to
 * Object.prototype. For example, a literal object such as `{"yes": "value"}`.
 * Or instances of `Object` like `new Object()`. Alternative, an object with
 * no prototype.
 *
 * @param {*} item - Item to check for object literal
 * @returns {boolean}
 */
function isPlainObject(item) {
  return toString(item) === objectSignature && _checkPlainObjectPrototype(item);
}

// Helper to verify that an object is indeed of type object.
// Ensure the object is either a literal object or an object instance created
// with `new Object()`. Or an object with no prototype.
function _checkPlainObjectPrototype(item) {
	const prototype = Object.getPrototypeOf(item);
	return prototype === null || prototype === Object.prototype;
}

/**
 * Check if input is an error
 *
 * @param {*} item - Item to check for error
 * @returns {boolean}
 */
function isError(item) {
  return toString(item) === errorSignature || item instanceof Error;
}

/**
 * Extract the type name. This uses Object.prototype.toString
 * to get the type name.
 *
 * @param {*} item - Item to get the type for
 * @returns {string} type of the object
 */
function typeName(item) {
  if (isNull(item)) {
    return "null";
  }
  else if (isUndefined(item)) {
    return "undefined";
  }

  return /\[.+ ([^\]]+)/.exec(toString(item))[1].toLowerCase();
}

module.exports = {
  isBoolean: isBoolean,
  isNull: isNull,
  isUndefined: isUndefined,
  isRegex: isRegex,
  isArray: isArray,
  isBuffer: isBuffer,
  isError: isError,
  isString: isString,
  isObject: isObject,
  isPlainObject: isPlainObject,
  isFunction: isFunction,
  isDate: isDate,
  isNumber: isNumber,
  typeName: typeName,
  toString: toString
};
