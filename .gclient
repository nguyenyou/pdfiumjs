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