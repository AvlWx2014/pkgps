# pkgps (Package GPS)

Package coordinates as proper types in Python.

The name "pkgps" is a portmanteau of sorts combining the abbreviated form of package (pkg) with 
the abbreviation for The Global Positioning System (gps).

Package coordinate systems allow software engineers and developers to uniquely identify a 
particular incarnation of a software package.

Some common examples:
* `NVR` - `name-version-release` family of coordinates for RPM packages on RPM-based linux 
  (including `NEVR`, `NEVRA`, and `NVRA`).
* `GAV` - `group:artifact:version` coordinates for Maven packages
* `Deb`- `package-upstream_version` coordinates for Debian packages (Debian package coordinates 
  don't have a punchy abbreviation like `NVR` or `GAV` I could find) 
* `PEP440` - [PEP 440](https://peps.python.org/pep-0440/) version specifications and dependency 
  identifiers

One common way to represent instances of coordinates in various package coordinate systems is as a 
string, which provides no additional information as to how that string is to be interpreted.

Take an example function that expects to find an RPM build from Fedora Koji based on its 
coordinates. An `NVR` has higher-precision counterparts like `NVRA` and `NEVRA`, so how do I 
disambiguate a string representing NVR coordinates from one representing `NVRA` or `NEVRA` 
coordinates?

```python
def get_package_build(coordinates: str) -> int:
    pass  
```

From the perspective of the type system, all we know about this function is that it takes a string 
and returns an integer. What does the input string mean? What about the output integer?

One way to attribute additional meaning to these types is through type aliases like this:

```python
NVR = str
BuildId = int

def get_package_build(coordinates: NVR) -> BuildId:
    pass
```

For the output integer returned by this function this might suffice, but for the input string 
representing package build coordinates we can do better.

From the author of `get_package_build`'s perspective, for example, what happens if the 
underlying implementation needs to use various dimensions of the input coordinates separately? 
Then they have to do:

```python
from __future__ import annotations

NVR = str

def _parse_nvr(coordinates: NVR) -> tuple[str, str, str]:
    name, version, release = coordinates.rsplit("-", maxsplit=2)
    return name, version, release
```

Now the author has a reusable function that will break down an instance of NVR coordinates in to 
its individual components, so at least this logic won't have to be inlined everywhere they need 
to decompose NVR coordinates. 

However, as a caller of `_parse_nvr` we still don't learn very much from a typing perspective about 
how the component strings are meant to be interpreted. Instead, we see a function of type `(str) -> 
tuple[str, str, str]` and it's up to us as the caller to have the domain knowledge to know that 
the component strings are `name`, `version`, and `release` and in that order.

Of course, documentation can improve this situation slightly:

```python
from __future__ import annotations

NVR = str

def _parse_nvr(coordinates: NVR) -> tuple[str, str, str]:
    """
    Decompose `name-version-release` formatted coordinates in to `name`,`version`, and `release`.
    """
    name, version, release = coordinates.rsplit("-", maxsplit=2)
    return name, version, release
```

However, from a typing perspective we still just see `(str) -> tuple[str, str, str]`. If the 
implementation of this function changes and the components are returned in a slightly different 
order, errors can go silently unnoticed. For example both `version` and `release` are strings. 
If `_parse_nvr` swaps the order components are returned in, or you mistype some unpacking 
assignment like `n, r, v = _parse_nvr(...)` a type checker cannot help you detect this bug since 
the resolved types for `r` and `v` are both `str`.

We can do even better by representing various coordinate systems as proper types. Enter: `pkgps`.

`pkgps` represents package coordinate systems as types, and the individual components of an 
instance of these coordinates are accessible using the names you would expect e.g. `NVR#name`, 
`NVR#version`, `NVR#release` etc.

Let's use `pkgps` to rewrite our `get_build_id` function from earlier:

```python
from pkgps import NVR


BuildId = int


def get_build_id(nvr: NVR) -> BuildId:
    ...
```

Now there's no mistaking how `nvr` is to be interpreted, and, by reusing our type alias from 
earlier, what the integer returned by this function represents.

Additionally, internally this function can decompose the input NVR as needed by accessing the 
properties of `NVR`:

```python
from pkgps import NVR

def get_build_id(nvr: NVR) -> BuildId:
    package_info = api.get_package_builds(package=nvr.name)
    ...
```

You can even decompose an `NVR` in to its components with Python's unpacking behavior:

```python
from pkgps import NVR

n, v, r = NVR.from_string("curl-8.6.0-7.fc40")
print(f"{n=} {v=} {r=}")
# n=curl v=8.6.0 r=7.fc40
```

It's worth noting, though, that while `pkgps` helps remedy many problems it cannot fully 
overcome the limitation of iterable unpacking mentioned earlier - namely that accidentally 
swapping dimensions on the left-hand side of the unpacking can result in subtle bugs. We could 
go the extra mile to implement value types for `Name`, `Version`, `Release`, etc but doing so 
would become unwieldy to maintain, especially as more coordinate systems are added to the API.

Instead, **`pkgps` guarantees not to break iteration order for its types within a major version** 
(preferably _ever_, but within a major version is a more attainable goal). In other words, 
starting in version `1.y.z` `pkgps` types like `NVR` and its higher precision counterparts 
unpack dimension-wise from left-to-right e.g. `name, version, release` for `NVR`, 
`name, epoch, version, release, architecture` for `NEVRA` etc and this is guaranteed not to 
change within major version `1`.
