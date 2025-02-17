{
  'variables': {
    'openssl_fips': '0',
  },
  "targets": [
    {
      "target_name": "native-registry",
      "msvs_settings": {
        "VCCLCompilerTool": { "ExceptionHandling": 1 },
      },
      "sources": [
        "src/addon.cc",
      ],
      "libraries": [
        "advapi32",
      ],
      "include_dirs": [
        "<!@(node -p \"require('node-addon-api').include\")",
      ]
    },
    {
      "target_name": "copy_binary",
      "type": "none",
      "dependencies": [ "native-registry" ],
      "copies": [
        {
          "destination": "<(PRODUCT_DIR)/../../dist",
          "files": [
            "<(PRODUCT_DIR)/native-registry.node",
          ]
        }
      ]
    }
  ]
}
