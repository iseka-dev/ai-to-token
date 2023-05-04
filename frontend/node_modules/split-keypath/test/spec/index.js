import splitKeypath from "src/index";
import { expect } from "chai";

describe("splitKeypath Suite", function() {
  describe("When resolving a simple", function() {
    var result;

    beforeEach(function() {
      result = splitKeypath("test");
    });

    it("then the resolved path contains the simple string", function() {
      expect(result).to.include("test");
    });
  });

  describe("When resolving a path with a key index", function() {
    var result;

    beforeEach(function() {
      result = splitKeypath("a[1]");
    });

    it("then the result contains the root path", function() {
      expect(result[0]).to.equal("a");
    });

    it("then the result contains the path with the array index value", function() {
      expect(result[1]).to.equal("1");
    });
  });

  describe("When resolving a path with a key index that is a paragraph", function() {
    var result, paragraph;

    beforeEach(function() {
      paragraph = "this is some really long path. With - dashes + some other odd %$& characters";
      result = splitKeypath("a[" + paragraph + "].b");
    });

    it("then the result contains the root path", function() {
      expect(result[0]).to.equal("a");
    });

    it("then the result contains the long paragraph", function() {
      expect(result[1]).to.equal(paragraph);
    });

    it("then the result contains a key after the long paragraph", function() {
      expect(result[2]).to.equal("b");
    });
  });
});
