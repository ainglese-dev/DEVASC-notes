# Compare Data Formats

## XML

### Componets

- Tag: Markers similar to HTML tags that identify elements within an XML document
- Attribute: Key-value pair nexted in the opening tag
- Element: Everything contained within an opening and closing tag (can contain subelements)

### Example Structure

```
<RootTag>
  <SubTag Attribute="attr1">
      <SubSubTag1>Value</SubSubTag1>
      <SubSubTag2>Value</SubSubTag2>
  </SubTag>
</RootTag
```

## JSON

### Components

- String: A series of text characters wrapped in quotes
- Number: A numerical value
- Boolean: A true or false value (always lowercase)
- Object: A grouping of one or more key/value pairs
- Array: A list of elements

### Example Structure

```
{
  "root_object": {
    "array": [
      "element1",
      "element2"
    ],
    "object": {"key": "value" }
  }
}
```

## YAML

### Components

- String: A series of text characters that may or may not be wrapped in quotes
- Number: A numeric integer value
- Float: A numeric floating-point decimal value
- Boolean: A true or false value (multiple upper/lowercase permutations allowed)
- List/array: A series of elements
- Mapping: A key/value pair

### Structure

```
---
mapping:
- ListID: 1
  Key: "Value"
  Active: True
- ListID: 2
  Key: "Value"
  Active: False
...
```
