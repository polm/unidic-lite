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

## Differences from the Official UniDic Release

This has a few changes from the official UniDic release to make it easier to use.

- entries for 令和 have been added
- single-character numeric and alphabetic words have been deleted
- `unk.def` has been modified so unknown punctuation won't be marked as a noun

## License

This code is licensed under the MIT or WTFPL license, as you prefer. Unidic
2.1.2 is copyright the UniDic Consortium and distributed under the terms of the
[BSD license](./LICENSE.unidic). 
