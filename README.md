# PDFiumJS

## How to compile a wasm

### Create a `.gclient` file

```
solutions = [
  { "name"        : 'pdfium',
    "url"         : 'https://pdfium.googlesource.com/pdfium.git',
    "deps_file"   : 'DEPS',
    "managed"     : False,
    "custom_deps" : {
    },
    "custom_vars": {'checkout_configuration': 'minimal'},
  },
]
target_os = [ 'emscripten' ]
```

### Fetch the source

```
gclient sync -r origin/chromium/6815 --no-history --shallow
```

Or latest

```
gclient sync -r origin/main --no-history --shallow
```

### Patch sources

We can't compile it yet, we need to modify the source in order to be compiled to wasm.