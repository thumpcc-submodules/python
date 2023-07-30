import requests
import kerberos
import dns.resolver

from requests.compat import urlparse


def myrequests_request(method, url, client_principal=None, **kwargs):
    req = requests.request(method, url, **kwargs)
    if "Negotiate" in req.headers.get("www-authenticate", ""):
        hostname = urlparse(req.url).hostname
        canonical_name = dns.resolver.Resolver().query(hostname).canonical_name
        ret_code, context = kerberos.authGSSClientInit(f"HTTP@{canonical_name}", principal=client_principal)
        kerberos.authGSSClientStep(context, "")
        kwargs["headers"] = {**kwargs.get("headers", {}),
                             **{"Authorization": f"Negotiate {kerberos.authGSSClientResponse(context)}"}}
        req = requests.request(method, req.url, **kwargs)
    return req


myrequests_get = lambda url, **kwargs: myrequests_request('GET', url, **kwargs)
myrequests_post = lambda url, **kwargs: myrequests_request('POST', url, **kwargs)

req = myrequests_get("http://your.server.com/")
