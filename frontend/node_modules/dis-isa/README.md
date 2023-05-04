## dis isa

> isa types for javascript

### API


#### isBoolean(any) : boolean

Method that takes in a value and returns whether or not it is boolean.

``` javascript
import types from 'dis-isa';

types.isBoolean(true); // true
types.isBoolean(false); // true
types.isBoolean(1); // false
types.isBoolean(undefined); // false
```

#### isUndefined(any) : boolean

Method that takes an input and returns whether or not it is `undefined`.

``` javascript
import types from 'dis-isa';

types.isUndefined(1); // false
types.isUndefined(undefined); // true
```

#### isNull(any) : boolean

Method that takes an input and returns whether or not it is `null`

``` javascript
import types from 'dis-isa';

types.isNull(1); // false
types.isNull(null); // true
types.isNull(undefined); // false
```

#### isRegex(any) : boolean

Method that takes an input and returns whether or not it is a regular expression

``` javascript
import types from 'dis-isa';

types.isRegex(1); // false
types.isRegex(/some/); // true
types.isRegex(new RegExp('some')); // true
```

#### isArray(any) : boolean

Method that takes an input and returns whether or not it is an array. The check will try to default to the built in `isArray` if available, otherwise an equivalent check is performed.

``` javascript
import types from 'dis-isa';

types.isArray(1); // false
types.isArray([]); // true
types.isArray(new Array()); // true
```

#### isFunction(any) : boolean

Method that takes an input and returns whether or not it is a function.

``` javascript
import types from 'dis-isa';

function test() {
}

types.isFunction(1); // false
types.isFunction(test); // true
types.isFunction(new test()); // false
```

#### isString(any) : boolean

Method that takes an input and returns whether or not it is a string.

``` javascript
import types from 'dis-isa';

types.isString(1); // false
types.isString("test"); // true
types.isString(new String("test")); // true
```

#### isDate(any) : boolean

Method that takes an input and returns whether or not it is a Date.

``` javascript
import types from 'dis-isa';

types.isDate(1); // false
types.isDate("test"); // false
types.isDate(new Date()); // true
```

#### isObject(any) : boolean

Method that takes an input and returns whether or not it is an object. And object is any one of the following:
- literal object
- object instance
- array
- null

``` javascript
import types from 'dis-isa';

types.isObject(1); // false
types.isObject("test"); // true
types.isObject(new String("test")); // true
types.isObject(null); // true
```

#### isPlainObject(any) : boolean

Method that takes an input and returns whether or not it is a plain object. A plain object can be:
- A literal object. `{}`
- Objects created with `new Object()` and `Object.create`

``` javascript
import types from 'dis-isa';

types.isPlainObject(1); // false
types.isPlainObject("test"); // false
types.isPlainObject(new Object()); // true
types.isPlainObject(Object.create(null)); // true
types.isPlainObject({}); // true
```

#### isError(any) : boolean

Method that takes an input and returns whether or not it is an Error. Errors are instances of `Error`, including exceptions.

``` javascript
import types from 'dis-isa';

var err = new Error();

types.isError(1); // false
types.isError(err); // true
```

#### typeName(any) : string

Method that takes an input and returns its string type representation. The string type is all lower case. Useful for extending the supported types.

``` javascript
import types from 'dis-isa';

types.typeName(1); // 'number'
types.typeName(null); // 'null'
types.typeName(function() {}); // 'function'
```

#### toString(any) : string

Method that takes an input and returns the raw type signature. Useful for extending the supported types.

``` javascript
import types from 'dis-isa';

types.toString(1); // '[object Number]'
types.toString(null); // '[object Null]'
types.toString(function() {}); // '[object Function]'
```


### Licensed under MIT
