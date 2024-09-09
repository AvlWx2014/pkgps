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
