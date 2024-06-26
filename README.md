# HoudiniUnityAnimationClip
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://github.com/tanitta/HoudiniUnityAnimationClip/blob/main/LICENSE)
![image](https://github.com/tanitta/HoudiniUnityAnimationClip/assets/1937287/83629ac4-e11d-420a-883c-ac5a2e578acd)

## Description

This package consists of HDAs that directly export AnimationClips from Houdini to Unity.

- Unity Animation Clip Exporter ROP
- Unity Animation Clip Exporter SOP

## Installation

There are two ways to install this package: by using [Houdini venv Loader](https://github.com/tanitta/hvenvloader) and by installing it directly as a traditional [Houdini Package](https://www.sidefx.com/docs/houdini/ref/plugins.html).

### Installation using [Houdini venv Loader](https://github.com/tanitta/hvenvloader) (Recommended experimentally)

1. Install [Houdini venv Loader](https://github.com/tanitta/hvenvloader) and setup project.
2. Add this package to your project. e.g. using rye: `$ rye add HoudiniUnityAnimationClip --git https://https://github.com/tanitta/HoudiniUnityAnimationClip`
3. Reload .hip file into Houdini.

### Installation directry as [Houdini Package](https://www.sidefx.com/docs/houdini/ref/plugins.html)

1. Clone This Repository
2. Copy and paste `src/HoudiniUnityAnimationClip` into your `$HOUDINI_PREF_DIR/packages`.
3. Copy and paste `src/HoudiniUnityAnimationClip/HoudiniUnityAnimationClip.json` in it into `$HOUDINI_PREF_DIR/packages`.
4. Install python package: `PyYAML` in Houdini. 

cf. [Houdini packages | Houdini help](https://www.sidefx.com/docs/houdini/ref/plugins.html)
