# PYBAG

Python wrapper for [CBAG](https://github.com/bluecheetah/cbag) library.

This is a fork of [PYBAG] (https://github.com/ucb-art/pybag), which as of May 13th, 2019,
has been taken offline temporarily.

## Installation

### With OpenAccess

By default, installation uses OpenAccess, and can be performed with:

```bash
python -m pip install .
```

### Without OpenAccess

To install without OpenAccess edit the `setup.cfg` file:

```ini
[build_ext]
 ...
openaccess = disable
```

## Licensing

This library is licensed under the Apache-2.0 license.  However, some source files are licensed
under both Apache-2.0 and BSD-3-Clause license, meaning that the user must comply with the
terms and conditions of both licenses.  See [here](LICENSE.BSD-3-Clause) for full text of the
BSD license, and [here](LICENSE.Apache-2.0) for full text of the Apache license.  See individual
files to check if they fall under Apache-2.0, or both Apache-2.0 and BSD-3-Clause.
