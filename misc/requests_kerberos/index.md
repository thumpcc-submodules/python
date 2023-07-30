# Requests and Kerberos

The basic flow of a typical Kerberos authentication is as follows:

- Client sends an unauthenticated request to the server
- Server sends back a 401 response with a `WWW-Authenticate: Negotiate` header with no authentication details
- Client sends a new request with an `Authorization: Negotiate` header
- Server checks the `Authorization` header against the Kerberos infrastructure and either allows or denies access
  accordingly. If access is allowed, it should include a `WWW-Authenticate: Negotiate` header with authentication
  details in the reply.
- Client checks the authentication details in the reply to ensure that the request came from the server

A sample Python code using [Requests](https://requests.readthedocs.io/en/latest/)
and [Kerberos](https://github.com/apple/ccs-pykerberos/blob/master/pysrc/kerberos.py), {download}`requests_kerberos.py`:

```{literalinclude} requests_kerberos.py
:class: full-width
```

Before running above script, you need to obtain and cache Kerberos ticket-granting tickets (using kinit)

How to create keytab file and run kinit with it

```shell
kutil -v -k your.keytab.kt add -p User@your.domain -V 0 -e arcfour-hmac-md5
kinit -kt your.keytab.kt User@your.domain
```

References:

- [Using the Python Kerberos Module](http://python-notes.curiousefficiency.org/en/latest/python_kerberos.html)
- [requests-kerberos](https://github.com/requests/requests-kerberos)
- [rfc4559: SPNEGO-based Kerberos and NTLM HTTP Authentication in Microsoft Windows](https://tools.ietf.org/html/rfc4559)
- [apple/ccs-pykerberos/pysrc/kerberos.py](https://raw.githubusercontent.com/apple/ccs-pykerberos/master/pysrc/kerberos.py)
- <https://web.mit.edu/kerberos/>
- <https://kb.iu.edu/d/aumh>

