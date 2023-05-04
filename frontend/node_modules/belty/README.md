# belty

[![Greenkeeper badge](https://badges.greenkeeper.io/MiguelCastillo/belty.svg)](https://greenkeeper.io/)

General purpose utility belt

> as of v5.0.0, belty only generates a minified bundle `dist/index.js`.

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [API](#api)
  - [identity(arg?)](#identityarg)
  - [noop](#noop)
  - [pick(input, keys)](#pickinput-keys)
  - [omit(input, keys)](#omitinput-keys)
  - [assign(target, ...sources, transform)](#assigntarget-sources-transform)
  - [merge(target, ...sources, transform)](#mergetarget-sources-transform)
  - [isMatch(input, criteria)](#ismatchinput-criteria)
  - [find(input, predicate)](#findinput-predicate)
  - [findAll(input, predicate)](#findallinput-predicate)
  - [value(input, keypath, transform)](#valueinput-keypath-transform)
  - [values(input)](#valuesinput)
  - [toArray(...)](#toarray)
  - [arrayToObject(input, val)](#arraytoobjectinput-val)
- [License](#license)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# API

## identity(arg?)

Helper method that returns the first argument passed in.

- **@param** {*?} input - Argument to be returned. This is completely optional
- **@returns** {*} This returns whatever is passed in.

``` javascript
var input = 3.14;
assert(identity(input) === input);
```

<hr style="border-bottom: 1px solid #dedede;"/>

## noop

noop method! It takes no arguments and does not return anything. Useful when you need to setup an initial placeholder function.

``` javascript
var input = 3.14;
assert(noop(input) === undefined);
```

<hr style="border-bottom: 1px solid #dedede;"/>

## pick(input, keys)

> Alias `pluck`

Method that extracts key value pairs from the input object.

- **@param** {object} *input* - Object to generate data from.
- **@param** {string|string[]|object} *keys* - Key/value pairs to extract from `input`. Keys that do not exist in the input are ignored.
- **@returns** {object} Object with key value pairs of only the matching *keys*.


``` javascript
var input = {
  first: "Mgnum",
  last: "Rusty",
  id: "some-random-id"
};

var result = pick(input, ["first", "id", "something that does not exist"]);

// result is:
// {
//   first: "Mgnum",
//   id: "some-random-id"
// }
```

<hr style="border-bottom: 1px solid #dedede;"/>

## omit(input, keys)

Pulls out all the items in the input that are **not** in `keys` and returns a new object with just that.

Opposite of *pick*

- **@param** {object} *input* - Object to generate data from.
- **@param** {string|string[]|object} *keys* - Key/value pairs to exclude from `input`.
- **@returns** {object} Object with key value pairs without the matching *keys*.


``` javascript
var input = {
  first: "Mgnum",
  last: "Rusty",
  id: "some-random-id"
};

var result = omit(input, ["first"]);

// result is:
// {
//   last: "Rusty",
//   id: "some-random-id"
// }
```

<hr style="border-bottom: 1px solid #dedede;"/>

## assign(target, ...sources, transform)

> Alias `extend`


Shallow copies all properties from the input objects (sources) into the target object. Source objects are processed left to right overriding whatever values already exist in the result.

- **@param** {object} *target* - Object to copy properties to.
- **@param** {...} *source* - The source objects to be merged into the target object.
- **@param** {function} *transform* - Transform function called with current and next value in order to generate the final value for the particular object entry.

- **@returns** {object} Object with all source objects merged in.


``` javascript
var input1 = {
  first: "Mgnum",
  last: "Rusty",
  id: "some-random-id"
};

var input2 = {
  address: {
    street: "somewhere st",
    zip: "12345"
  }
};

var result = assign({}, input1, input2);

// result is a shallow copy of the input. So changing anything in address
// in the result will also change input.
//{
//  first: "Mgnum",
//  last: "Rusty",
//  id: "some-random-id",
//  address: {
//    street: "somewhere st",
//    zip: "12345"
//  }
//}
```

<hr style="border-bottom: 1px solid #dedede;"/>

## merge(target, ...sources, transform)

Deep copy all properties from the input objects (sources) into the target object. It merges objects and arrays into new structures from left to right overriding all other non array/object properties.

- **@param** {object} *target* - Object to copy properties to
- **@param** {...object} *sources* - The list of source objects to be merged into the target object
- **@param** {function} *transform* - Transform function called with current and next value in order to generate the final value for the particular object entry. The transform is only called with top level objects currently being processed.
- **@returns** {object} Object with all source objects merged in.

``` javascript
var source1 = {
  data: [1, 2, 3],
  misc: "random"
};

var source2 = {
  data: [4, 5]
};

var result = merge({}, source1, source2);

// {
//   data: [4, 5, 3],
//   misc: "modded"
// }
```

``` javascript
var source1 = {
  data: [1, 2, 3],
  misc: "random"
};

var source2 = {
  data: [4, 5, 6]
};

var result = merge({}, source1, source2, transform);

function transform(current, next) {
  if (Array.isArray(next.data)) {
    return {
      data: current.data ? current.data.concat(next.data) : next.data
    };
  }

  return next;
}

// The result of this is an object with the array entries concatinated
// and the exapnded out object property as generated by the transform
// method.
// {
//   data: [1, 2, 3, 4, 5, 6],
//   misc: "random"
// }
```

<hr style="border-bottom: 1px solid #dedede;"/>

## isMatch(input, criteria)

Deep comparisson of object structures recursively matching all properties in criteria with the input. If everything in the criteria matches the input, then isMatch returns true. Otherwise it returns false.

When matching items in an array, the index position is taken into account.

- **@param** {object | array | string | number} input - Object to check the criteria against
- **@param** {object | array | string | number} criteria - Object with all the data to match against
- **@returns** { boolean }


``` javascript
var input = {
  prop1: 3.14,
  prop2: [4, 8],
  prop3: {
    "prop3--1": [23]
  }
};

// Result is true
isMatch(input, {
  prop1: 3.14
});

// Result is true
isMatch(input, {
  prop2: [4]
});

// Result is false
isMatch(input, {
  prop2: [8]
});

// Result is false
isMatch(input, {
  prop2: [1]
});

// Result is true
isMatch(input, {
  prop3: {
    "prop3--1": [23]
  }
});
```

<hr style="border-bottom: 1px solid #dedede;"/>

## find(input, predicate)

Find the first item in the input for which the predicate function returns true for. When the predicate is not a function, isMatch is called with the predicate as the matching criteria.

Predicate functions are called with item, index, and original collection.

- **@param** { object | array } input - Collection of items to search in.
- **@param** { object | array | string | number | function } predicate - When the predicate is a function then that is called. Otherwise, isMatch is used to deeply match object structures. The result is the first item the predicate returns true for.
- **@returns** { Object } First item to match the predicate

Example with an input array

``` javascript
var input = [{
  city: "DET",
  number: 313
}, {
  city: "RO",
  number: 2311
}, {
  city: "DET",
  number: 734
}];

// Result is
// { city: "DET", number: 313 }
findAll(input, {
  city: "DET"
});
```

Example with an input object

``` javascript
var input = {
  item1: {
    city: "DET",
    number: 313
  },
  item2: {
    city: "RO",
    number: 2311
  },
  item3: {
    city: "DET",
    number: 734
  }
};

// Result is
// { city: "DET", number: 313 }
findAll(input, {
  city: "DET"
});
```

<hr style="border-bottom: 1px solid #dedede;"/>

## findAll(input, predicate)

Returns an array with all the items for which the predicate function returns true for. Or in the case when the predicate is not a function, isMatch is called with predicate as the matching criteria.

Predicate functions are called with item, index, and original collection.

- **@param** { object | array } input - Collection of items to search in.
- **@param** { object | array | string | number | function } predicate - When the predicate is a function then that is called. Otherwise, isMatch is used to deeply match object structures. The result is a collection of all the items the predicate returns true for.
- **@returns** { array } Collection of items that match the predicate.


Example with an input array

``` javascript
var input = [{
  city: "DET",
  number: 313
}, {
  city: "RO",
  number: 2311
}, {
  city: "DET",
  number: 734
}];

// Result is
// [{ city: "DET", number: 313 }, { city: "DET", number: 734 }]
findAll(input, {
  city: "DET"
});
```

Example with an input object

``` javascript
var input = {
  item1: {
    city: "DET",
    number: 313
  },
  item2: {
    city: "RO",
    number: 2311
  },
  item3: {
    city: "DET",
    number: 734
  }
};

// Result is
// [{ city: "DET", number: 313 }, { city: "DET", number: 734 }]
findAll(input, {
  city: "DET"
});
```

<hr style="border-bottom: 1px solid #dedede;"/>

## value(input, keypath, transform)

> Alias objectValue

Extract the value from an input object for the given keypath.

- **@param** {object} input - Object to read `property` from.
- **@param** {string|number|array} keypath - keypath for the value in the object.
- **@param** {function?} transform - Function that is called to transform the result. The function is called with the result, keypath and the input. The result from calling the transform is returned.
- **@returns** {*} The value for the corresponding keypath.


``` javascript
var input = {
  car: {
    interior: {
      seats: {
        count: 2,
        color: "blue"
      }
    }
  }
};

var result = value(input, ["car", "interior", "seats"]);

// result is the seats
// {
//   count: 2,
//   color: "blue"
// }
```

<hr style="border-bottom: 1px solid #dedede;"/>

## values(input)

> Alias objectValues

Gets the values from a object map and returns them in an array. If an array is passed in, then the array is returned as is.

- **@param** {object | Array} input - Input to get values from
- **@returns** { Array } - Array of all the values extracted from the input object, or the array itself if the input is an array.


``` javascript
var input = {
  "foo": "bar",
  "hello": "world"
};

var result = values(input);

// result is an array with just the object values
// ["bar", "world"]
```

<hr style="border-bottom: 1px solid #dedede;"/>

## toArray(...)

Converts input items to an array.

> When the input is an array, the items in it are added to the final resulting array.

- **@param** { * } input - Data to be converted to array
- **@returns** { array }

When the input is an object

``` javascript
var input = {
  a: "First value",
  b: "Second value"
};

var result = toArray(input);

// result is an array with the object as its values
[{
  a: "First value",
  b: "Second value"
}]
```

When the input is an array

``` javascript
var input = [{
  a: "First value",
  b: "Second value"
}];

var result = toArray(input);

// result is an array with the object as its values
[{
  a: "First value",
  b: "Second value"
}]
```

When the input is one object and an array

``` javascript
var input1 = {
  a: "First value",
  b: "Second value"
};

var input2 = [{
  c: "Third value",
  d: "Fourth value"
}, {
  e: "Fifth value",
  f: "Sixth value"
}];

var result = toArray(input1, input2);

// result is an array with the object as its values
[{
  a: "First value",
  b: "Second value"
}, {
  c: "Third value",
  d: "Fourth value"
}, {
  e: "Fifth value",
  f: "Sixth value"
}]
```

<hr style="border-bottom: 1px solid #dedede;"/>

## arrayToObject(input, val)

Converts arrays to a literal objects with the array values as keys. You can optionally pass in a callback function that is called in order to generate the values that go in the final result. `val` can also just be anything to be used as the value for each entry in the final result, otherwise `true` is used.

This method is useful in situation where you need to create a lookup table such as an object map (enums).

- **@param** { array } input - Items to convert to a map
- **@param** { *? } val - Can be a function, in which case it is called with the currect item in the array being processed in order to derive the value for the map entry. If a value of any other type is provided, that is used for populating each entry in the resulting map. Or if a value is not provided, all entries will be initialized to `true`
- **@returns** { object } Object will all the array values as keys and the derived values.


``` javascript
var input = ["first", "last", "GPS", "location"];
var result = arrayToObject(input);

// result is an object with the array items as the the keys for the object
// {
//   "first": true,
//   "last": true,
//   "GPS": true,
//   "location": true
// }
```

``` javascript
var input = ["first", "last", "GPS", "location"];
var result = arrayToObject(input, 3.14);

// result is an object with the array items as the the keys for the object
// {
//   "first": 3.14,
//   "last": 3.14,
//   "GPS": 3.14,
//   "location": 3.14
// }
```


``` javascript
var input = ["first", "last", "GPS", "location"];
var result = arrayToObject(input, transform);

function transform(value, key, array) {
  return value + "-" + key;
}

// result is an object with the array items as the the keys for the object
// {
//   "first": "first-0",
//   "last": "last-1",
//   "GPS": "GPS-2",
//   "location": "location-3"
// }
```

<hr style="border-bottom: 1px solid #dedede;"/>

# License

Licensed under MIT
