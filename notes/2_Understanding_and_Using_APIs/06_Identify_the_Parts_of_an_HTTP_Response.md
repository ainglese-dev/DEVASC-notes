# Identify the Parts of an HTTP Request and Response

## Both Request and Response

### Headers

- Set of k/v pairs
- Used to transmit metadata
- Not meant to transmit data

### Request Only

#### Querystring

- Series of k/v pairs appended to the URL
- Starts with a `?`
- k/v pairs concatented by `&`
- Usually used with GET requests

#### Payload

- Transmit large chunks of data to or from server
- Formatted as JSON, XML, HTML, etc
- Used with POST, PUT, PATCH

### Response Only

#### Response Code

An integer containing the result of the requested operation

#### Body

The payload of the response usually in the format requested in the initial request (json, xml, etc)


# HTTP Bonus Material

/Methods

## GET

CRUD: Read

- Used to read or retrieve a representation of a resource
- Not to be used to change data
- Can be considered safe and idempotent
- Can be cached
- Remain in browser history
- Can be bookmarked
- Should never be used with sensitive data
- Have length restrictions

## POST

CRUD: Create

- Used to create new resources
- Neither safe nor idempotent
- Never cached
- Do not remain in browser history
- Cannot be bookmarked
- No restrictions on data length

## PUT

CRUD: Update/Replace

Used to update a resource, but can also be used to create a resource if passed to a URI that contains a non-existent resource ID since the entire resource needs to be passed.

- Not considered a safe method in that it creates state
- Can be idempotent unless the operation updates e.g. a "last-updated" field.

## PATCH

CRUD: Update/Modify

Used to update a resource by passing only the values of the resource that need updating. Neither safe nor idempotent.

## DELETE

CRUD: Delete

Used to delete a resource identified by a URI. Usually idempotent.

## HEAD

CRUD: Read

Almost identical to GET, but no response body is returned. Useful to view what would be returned before making an expensive call to the API (e.g. large response body expected).

## OPTIONS

CRUD: Read

Describes the communication options for the target resource.
