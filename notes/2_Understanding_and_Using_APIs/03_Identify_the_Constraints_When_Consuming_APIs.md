# Identify the Constraints When Consuming APIs

## REST

- Uniform interface
  - All actions should occur at the same URL (e.g. `/movies/{movieID}` with `/update` or `/delete` appended
  - Transport needs to be consistent (i.e. can't have HTTPS for some endpoints and FTP for others)
- Client-server
  - All communication must happen between the API interface
- Stateless
  - Every API call must have all the information required to perform the requested operation
  - Server does not 'remember' the client from request to request
