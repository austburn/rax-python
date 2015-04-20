from setuptools import setup

setup(
    name="rax-python",
    description="Rackspace Python class witht Glyph Lefkowitz",
    packages=[
        "rax"
    ],
    install_requires=[
        "requests[security]"
    ],
    license="MIT",
    version="0.0.1",
    entry_points = {
        "console_scripts": [
            "say-hello=entry:some_func"
        ]
    },
    package_data = {
        '': ['*.data']
    }
)