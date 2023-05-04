var pick = require("./pick");
var omit = require("./omit");
var assign = require("./assign");
var merge = require("./merge");
var findAll = require("./findAll");
var identity = require("./identity");
var isMatch = require("./isMatch");
var noop = require("./noop");
var arrayToObject = require("./arrayToObject");
var value = require("./value");
var values = require("./values");
var toArray = require("./toArray");

module.exports = {
  result: value,
  pluck: pick,
  pick: pick,
  omit: omit,
  assign: assign,
  extend: assign,
  merge: merge,
  findAll: findAll,
  identity: identity,
  isMatch: isMatch,
  noop: noop,
  value: value,
  values: values,
  objectValue: value,
  objectValues: values,
  arrayToObject: arrayToObject,
  toArray: toArray
};
