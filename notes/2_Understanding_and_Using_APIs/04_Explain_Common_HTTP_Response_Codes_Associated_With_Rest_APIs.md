# Explain Common HTTP Respnonse Codes Associated with REST APIs

## Success

### 200 OK

Standard response for successful HTTP requests. Actual response will depend on the HTTP verb used:

- GET: response contains the entity corresponding to the requested resource
- POST: response containes an entity describing or containing the result of the action

### 201 Created

The request has been fulfilled, resulting the the creation of a new resource.

### 202 Accepted

The request has been accepted for processing, but processing has not been completed.

Asynchronous API calls.

### 204 No Content

The server has successfully processed the request and is not returning any content.

Common with DELETE reqests.

## Redirection

### 301: Moved Permanently

This and all future requests should be directed to the given URL.

### 302: Found

Previously "Moved Temporarily"; has been superceeded by 303 and 307, but many browsers and frameworks use 302 as 303.

### 303: See Other

The response can be found under another URI using the GET method. If 303 is received when using a PUT, POST, PATCH, etc it can be assumed that GET should be used instead.

### 307: Temporary redirect

The request should be repeated with the specified URI; however subsequent calls will still use the original URI. The method/verb is not allowed to be changed when reissuing the request (e.g. a POST cannot be repeated using a GET).

## Client Errors

### 400: Bad Request

The server cannot or will not process the request due to malformed request, request too large, etc.

### 401: Unauthorized

The request requires authentication that has either not been provided or for which invalid credentials have been provided.

### 403: Forbidden

The request is valid, however the server is refusing to take action. Usually related to permissions issues either with the authenticated user or file permissions on the server.

### 404: Not Found

The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible.

### 418: I'm a Teapot

LOL response code from a an April Fool's RFC.

### 429: Too Many Requests

The user has sent too many requests in a set amount of time. Utilized with rate limiting features.

### 451: Unavailable for Legal Reasons

The server operator has received a legal demand to deny access to the resource. 451 is a reference to Fahrenheit 451.

## Server Errors

### 500: Internal Server Error

Generic error message for when an unexpected condition is encountered with no more specific message suitable.

### 501: Not Implemented

The server does not recognize the request method or is unable to fulfil the request. Usually implies the method will be available in the future.

### 502 Bad Gateway

The server is acting as a gateway or reverse proxy and received an invalid response from the upstream server/service.

### 503: Service Unavailable

The server cannot handle the request (overloaded, down for maintenance, etc). Usually temporary.
