[![Current PyPI packages](https://badge.fury.io/py/unidic-lite.svg)](https://pypi.org/project/unidic-lite/)

# Unidic Lite

This is a version of [unidic-py](https://github.com/polm/unidic-py) that is
designed to be installable with pip alone, not requiring any extra downloads. 

At the moment it uses Unidic 2.1.2, from 2013, which is the most recent release
of UniDic that's small enough to be distributed via PyPI.

**Note this package takes roughly 250MB on disk after being installed.**

In order to use this you will need to install a MeCab wrapper such as
[mecab-python3](https://github.com/SamuraiT/mecab-python3) or
[fugashi](https://github.com/polm/fugashi). 

## License

This code is licensed under the MIT or WTFPL license, as you prefer. Unidic
2.1.2 is distributed under the GPL2, LGPL, or BSD license.
