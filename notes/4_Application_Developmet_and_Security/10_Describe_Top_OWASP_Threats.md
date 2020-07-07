# Describe Top OWASP Threats

#### Cross-site Scripting

Category: Injection

Summary: Malicious script is injected into an otherwise-trusted website e.g. in a comment section. The script is run by the browsers of subsequent users that load the page.

Prevention: Escape javascript and HTML elements

#### SQL Injection

Category: Injection

Summary: User maliciuosly adds raw SQL statements into an input in an attempt to directly interact with the database.

Prevention: User parepared statements and stored procedures and escape all user-supplied input

#### Cross-site Request Forgery

Category: 

Summary: Forces an end user to execute unwanted actions on a web application to which they are already authenticated. Examples include transferring funds or changing the email address on the account.

Prevention: Use the framework's built-in CSRF protection if available, use custom headers, use CSRF tokens
