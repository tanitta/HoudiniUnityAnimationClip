from setuptools import setup, find_packages

setup(
    name='HoudiniUnityAnimationClip',
    version="0.0.1",
    description="This package consists of HDAs that directly export AnimationClips from Houdini to Unity.",
    author='tanitta',
    packages=find_packages(),
    license='Apache License 2.0',
    install_requires=[
        'yaml'
    ]
)
