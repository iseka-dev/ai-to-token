# split-keypath
> Splits strings into an array of keys used for reading nested data structures

split-keypath is a method that takes a string as an input and generates an array of keys that can be used for reading values from a deeply nested object.  The algorithm supports extracting array keys, which is how you can specify arbitrary keys. Please see below for examples.


## Install

```
$ npm install split-keypath
```

> The npm package has a bundle for the browser


## Examples

``` javascript
import splitKeypath from "split-keypath";
var result = splitKeypath("hello.world");
// Result is ["hello", "world"]
```

``` javascript
import splitKeypath from "split-keypath";
var result = splitKeypath("hello[0].world[some really long string. with non ascii chars.]");
// Result is ["hello", "0", "world", "some really long string. with non ascii chars."];
```

Practical use that reads a value from a somewhat deeply nested object hierarchy

``` javascript
import splitKeypath from "split-keypath";

function readDeepValue(input, keypath) {
  return splitKeypath(keypath).reduce((nested, key) => nested[key], input);
}

var input = {
  some: {
    deep: [
      {
        key: 42
      }
    ]
  }
};

var result = readDeepValue(input, "some.deep[0].key");
// Result is 42
```


## License
MIT
