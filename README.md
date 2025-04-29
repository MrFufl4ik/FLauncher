# FLauncher

## Fast About
FLauncher - MC launcher, which is an add-on to [PortableMC](https://github.com/mindstorm38/portablemc), which has the ability to work with a remote `FTP` server for easy download and updating of the MC modpack.

## Compability
Flauncher launch on:
  * `Linux based system`
  * `Windows 10+`

## Where is Flauncher stored?
Flauncher stored in root of disk. The disk where the FLauncher will be stored is determined by the user.
### Example launcher path for windows
 `"C:/FLauncher"`
### Example launcher path for linux
 `/home/mrfufl4ik/FLauncher`

## Modpack managment
1. `Create` a modpack so easy. Run a `create` menu. To create a modpack, you specify an `id` and a text name (optional). This so easy :0
2. If modpack is not visiable, but you create it, use a `Refresh`. //ToDo add auto-refresh :)
3. `Configure` your modpack? Too easy. In list choose your modpack. Run a `configure` menu. In `configure` menu, you can edit the `player name`, `mc version`, `java args`, and `title name`. Empty input box, means `default` values.
After setting, use a `apply` button.

## Modpack structure

### Modpack path
The modpacks located in `/modpacks`. After that comes your modpack `id`. Example, modpack called: `mymodpack`. Means your modpack path: `/modpacks/mymodpacks`.

### Modpack client path
It is also worth considering that the modpack folder and the MC client folder are different things. Minecraft client folder defined: `client`, so `/modpacks/mymodpack/client` equal `.minecraft`, so this client minecraft folder.

### Modpack launcher file
File `launcher` important for FLauncher defined this modpack, if you want a self-create modpack, this file is so important to FLauncher.

### Modpack config file
Config file, used a `json` format. Settings has a 4 required input field: `username`, `loader`, `version`, `java_args`. If config or one of them is empty - FLauncher use a default field value.

Modpack config field's list:
 * `titlename`: string filed equal name visible in FLauncher modpacks list.
 * `username`: string field equal player name, used in MC.
 * `loader`: string field equal player MC modloader, used `portablemc`, to download and run MC.
 * `version`: string field equal MC version, used `portablemc`, to download and run MC.
 * `java_args`: string field equal java arguments used, to run MC.
 * `update_version`: integer number equal version of modpack, used `ftp` update system.

## How to download?
If you are using `windows`, you can used [FLauncherInstaller](https://github.com/MrFufl4ik/FLauncherInstaller)(More info there).

If you are using `linux` you have to follow the steps:
 1. Install `git` and `python`: `pacman -S git python` (example in Arch Linux based system).
 2. Clone repository: `git clone https://github.com/MrFufl4ik/FLauncher`.
 3. Install requirements `pip install -r requirements.txt`.

## Runner
in devolpment

## FLauncher & FLauncherInstaller state
FLauncher & FLauncherInstaller they are still being developed and are in active testing.
