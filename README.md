# HoudiniUnityAnimationClip

![image](https://github.com/tanitta/HoudiniUnityAnimationClip/assets/1937287/83629ac4-e11d-420a-883c-ac5a2e578acd)

## Description

This package consists of HDAs that directly export AnimationClips from Houdini to Unity.

- Unity Animation Clip Exporter ROP
- Unity Animation Clip Exporter SOP

## Installation

There are two ways to install this package: by using [hrye](https://github.com/tanitta/hrye) and by installing it directly as a traditional Houdini package.

### [hrye](https://github.com/tanitta/hrye) (Recomented)

1. Install [hrye](https://github.com/tanitta/hrye) and setup project.
2. `$ rye add HoudiniUnityAnimationClip --git https://https://github.com/tanitta/HoudiniUnityAnimationClip`
3. Reload .hip file into Houdini.

### Installation directry as Houdini Package

1. Clone This Repository into your `$HOUDINI_PREF_DIR/packages`.
2. Copy and paste `HoudiniUnityAnimationClip.json` in it into `$HOUDINI_PREF_DIR/packages`.
3. add python package to houdini. `$ hython -m pip install yaml`

cf. [Houdini packages | Houdini help](https://www.sidefx.com/docs/houdini/ref/plugins.html)
