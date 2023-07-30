# hash() on str and bytes objects

A {wikipedia}`Hash_function` is any function that can be used to map data of arbitrary size to fixed-size values, though there are some hash functions that support variable length output.

Starting Python 3.3, {py:func}`hash` is _salted_ with an unpredictable random value. Although it remains constant within an individual Python process, it's not predictable between every run of Python invocations.

```console
$ python -c 'print(hash("foo"))'
-9001231485817621307
$ python -c 'print(hash("foo"))'
98327169504980687
$ python -c 'print(hash("foo"))'
4787167050816198975
```

If {std:envvar}`PYTHONHASHSEED` is set to an integer value, it's used as a fixed seed for generating the hash.

```console
$ PYTHONHASHSEED=1 python -c 'print(hash("foo"))'
1603728720450038992
$ PYTHONHASHSEED=1 python -c 'print(hash("foo"))'
1603728720450038992
```

```{note}
[oCERT-2011-003](https://ocert.org/advisories/ocert-2011-003.html): Randomize hashes of str and bytes to protect against denial of service attacks due to hash collisions within the dict and set types
```

If you need to use hash for making verifiable checksums of files, use MD5, SHA256, etc. 

See also https://stackoverflow.com/a/17586126/9265323
