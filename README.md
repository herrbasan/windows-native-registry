# windows-native-registry

This is a fork of [windows-native-registry](https://github.com/Eugeny/windows-native-registry) by Eugene Pankov with additional improvements.

[![Node CI](https://github.com/herrbasan/windows-native-registry/actions/workflows/nodejs.yml/badge.svg)](https://github.com/herrbasan/windows-native-registry/actions/workflows/nodejs.yml)

* No external processes.
* Node-API
* Electron ready

```ts
export interface RegistryValue {
    name: string
    type: REG
    value: any
}

export enum HK {
    CR = 0x80000000,
    CU = 0x80000001,
    LM = 0x80000002,
    U = 0x80000003,
}

export enum REG {
    SZ = 1,
    EXPAND_SZ = 2,
    BINARY = 3,
    DWORD = 4,
}

export function getRegistryKey (root: HK, path: string): {[name: string]: RegistryValue}

export function getRegistryValue (root: HK, path: string, name: string): any

export function setRegistryValue (root: HK, path: string, name: string, type: REG, value: string): any

export function setRegistryValue (root: HK, path: string, name: string, type: REG.MULTI_SZ, value: string[]): any

export function listRegistrySubkeys (root: HK, path: string): string[]

export function createRegistryKey (root: HK, path: string)

export function deleteRegistryKey (root: HK, path: string)
```

Example Usage:
```js
const path = require('path');
const reg = require('../libs/native-registry.js');


async function registry(task, exe_path, app_path) {
    return new Promise(async (resolve, reject) => {
        let icon_path = path.join(path.dirname(app_path), 'icons');
        let registry_data = {
            app: {
                name: 'SoundApp',
                exe: path.basename(exe_path),
            },
            filetypes: {
                soundapp_mp3: {
                    description: 'SoundApp Audio File',
                    icon: 'mp3.ico',
                    extensions: ['mp3'],
                }
            }
        }
     
        if (task === 'register') {
            for (let key in registry_data.filetypes) {
                await reg.registerProgID({
                    progID: key,
                    description: registry_data.filetypes[key].description,
                    app_name: registry_data.app.name,
                    icon_path: path.resolve(icon_path, registry_data.filetypes[key].icon),
                    command: exe_path,
                    extensions: registry_data.filetypes[key].extensions,
                })
            }
        }
        else if (task === 'unregister') {
            for (let key in registry_data.filetypes) {
                await reg.removeProgID({ progID: key, extensions: registry_data.filetypes[key].extensions});
            }
        }
  
        resolve(true);
    });
}

```

## Changes from original
- Removed Typescript
- Added a function to delete values
- Added a convenience function to register ProgID's and file associations in one go.
- Added a convenience function to remove ProgID's and file associations in one go.
- Removed unwanted libraries
- Creates a N-API Modile alongside the Javascript in a dist folder to directly use them in electron Projects

## Contributors ✨
Original project by [Eugene Pankov](https://github.com/Eugeny)

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/cwalther"><img src="https://avatars1.githubusercontent.com/u/234094?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Christian Walther</b></sub></a><br /><a href="https://github.com/Eugeny/windows-native-registry/commits?author=cwalther" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/Sikkesoft"><img src="https://avatars.githubusercontent.com/u/11422479?v=4?s=100" width="100px;" alt=""/><br /><sub><b>André Sikma</b></sub></a><br /><a href="https://github.com/Eugeny/windows-native-registry/commits?author=Sikkesoft" title="Code">💻</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!

## License
MIT License - See [LICENSE](LICENSE) for details
