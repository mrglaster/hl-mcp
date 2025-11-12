# Building AMX Mod X
From AlliedModders Wiki
Jump to: [navigation](https://wiki.alliedmods.net/Building_AMX_Mod_X#mw-head), [search](https://wiki.alliedmods.net/Building_AMX_Mod_X#p-search)
AMX Mod X is a large project, but we've tried to make it as easy to build as possible. The directions here will step you through the entire process. 
## Contents
  * [1 Requirements](https://wiki.alliedmods.net/Building_AMX_Mod_X#Requirements)
    * [1.1 Windows](https://wiki.alliedmods.net/Building_AMX_Mod_X#Windows)
    * [1.2 Linux](https://wiki.alliedmods.net/Building_AMX_Mod_X#Linux)
    * [1.3 Mac OS X](https://wiki.alliedmods.net/Building_AMX_Mod_X#Mac_OS_X)
  * [2 Dependencies](https://wiki.alliedmods.net/Building_AMX_Mod_X#Dependencies)
  * [3 Configuring](https://wiki.alliedmods.net/Building_AMX_Mod_X#Configuring)
  * [4 Building](https://wiki.alliedmods.net/Building_AMX_Mod_X#Building)


# Requirements
## Windows
  1. Install Visual Studio or Visual C++ 2013 or higher. Express editions should work fine. Make sure to get the "Desktop" version: [Visual Studio](http://www.visualstudio.com/downloads/download-visual-studio-vs).
  2. Install [Git](http://git-scm.com/). Make sure that you select the option that adds Git to PATH.
  3. Install [Nasm](https://www.nasm.us/pub/nasm/releasebuilds/?C=M;O=D). Go the latest version, then choose either win32 or win64 directory. Optionally, add the Nasm to PATH. 
  4. Next, you will need to start an environment capable of running Python and interacting with the Visual Studio compiler. There are two ways to do this. 
     * Use [MozillaBuild 2.2.0](https://wiki.mozilla.org/MozillaBuild). MozillaBuild comes with Python, Mercurial, and a unix-like shell. Do not use version 3 and higher. 
       1. Install MozillaBuild.
       2. Navigate to `C:\mozilla-build` and run the batch file corresponding to your Visual Studio version. For example, `start-msvc13.bat` for Visual Studio 2013 (12.0). Do not run an x64 version.
       3. Add Git to MozillaBuild's `PATH`. The easiest way to do this is to enter the following commands: ```
echo "export PATH=\$PATH:/c/Program\ Files\ \(x86\)/Git/bin" >> ~/.profile
source ~/.profile

```

     * Or, you can manually set up a shell. 
       1. Install [Mercurial](https://www.mercurial-scm.org/).
       2. Install [Python](http://python.org/) 2.7. It will install to C:\Python27 by default. (Version 3.4 will work, but is not recommended for compatibility with other tools).
       3. Add Python to your `PATH` variable. Go to Control Panel, System, Advanced, Environment Variables. Add `C:\Python27;C:\Python27\Scripts` to `PATH` (or wherever your Python install is).
       4. Under Start, Programs, Microsoft Visual Studio, select the "Visual Studio Tools" folder and run "Visual Studio Command Prompt". Alternately, open a normal command prompt and run `"C:\Program Files (x86)\Microsoft Visual Studio 13.0\VC\bin\vcvars.bat"`. Substitute your Visual Studio version if needed.


Note that AMX Mod X also has Visual Studio project files. These can be used for local development, however, they are not maintained nor are they used for official builds. 
## Linux
  1. Install Git, via either system packages or from the [Git](http://git-scm.com/) distribution.
  2. Install either the GNU C Compiler or the Clang compiler. On Debian/Ubuntu, the following commands will give you everything: ```
sudo apt-get install gcc g++ clang nasm
  
```

  3. If building on a 64-bit system, a few additional packages may be required. For example on Debian/Ubuntu they are: ```
sudo apt-get install ia32-libs
sudo apt-get install lib32z1 lib32z1-dev
sudo apt-get install libc6-dev-i386 libc6-i386
sudo apt-get install gcc-multilib g++-multilib

```



## Mac OS X
Mac OS X 10.7 or higher is required to build, however, AMX Mod X will work on versions as early as 10.5. 
  1. Install the Xcode Command Line Tools. 
     * For OS X 10.9 or higher, run the command below in Terminal and click the Install button in the window that appears. ```
xcode-select --install

```

     * For earlier versions of OS X, download and install Xcode from the App Store. Launch Xcode and then navigate to Preferences -> Downloads -> Components -> Command Line Tools -> Install. If you have recently upgraded Xcode, you will need to perform this step again. AMX Mod X cannot build without Xcode's command line tools.


# Dependencies
Building AMX Mod X requires AMBuild, Metamod, the Half-Life SDK, and optionally MySQL 5.5. If you're using Linux, OS X, or Windows with MozillaBuild, you download and run the following script to get everything: 
```
https://raw.githubusercontent.com/alliedmodders/amxmodx/master/support/checkout-deps.sh
bash checkout-deps.sh

```

This will download everything required into `amxmodx`, `hlsdk`, and `metamod-am`. If AMBuild is not installed, it will also download it into `ambuild`, and prompt you for your password to install it. 
If for some reason this script doesn't work, or you can't use it, you can get AMX Mod X and its dependencies like so: 
```
git clone https://github.com/alliedmodders/ambuild
git clone https://github.com/alliedmodders/metamod-hl1
git clone https://github.com/alliedmodders/hlsdk
git clone --recursive https://github.com/alliedmodders/amxmodx
cd ambuild
python setup.py install     # May need sudo or root on Linux/OS X

```

# Configuring
The first time you are building AMX Mod X, you must _configure_ the build. First create a build folder, and then run `configure.py`. For example: 
```
mkdir build
cd build
python ../configure.py

```

It is safe to reconfigure over an old build. However, it's probably a bad idea to configure inside a random, non-empty folder. 
There are a few extra options you can pass to `configure`: 
  * `--enable-debug` - Compile with symbols and debug checks/assertions.
  * `--enable-optimize` - Compile with optimizations.
  * `--symbol-files` - Remove debugging symbols
  * `--no-mysql` - If you didn't install MySQL, you can choose not to build the extension.
  * `--hlsdk` - Custom path to HLSDK.
  * `--metamod` - Custom path to Metamod source code.
  * `--mysql` - Custom path to MySQL.
  * `--disable-auto-versioning` - Disable the auto-versioning script
  * `--nasm` - Path to Nasm. If you are under windows and you did not add Nasm to PATH, you can choose the location.


# Building
To build AMX Mod X, simply navigate to your build folder and type `ambuild`: 
```
cd build
ambuild

```

Alternately, you can specify the path of the build folder: 
```
ambuild build

```

The full package layouts that would be shipped for release are in the `package` folder of the build. 
