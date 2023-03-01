#!/bin/bash/
git clone https://github.com/GerbenJavado/LinkFinder.git ./Tools
cd ./Tools/LinkFinder && python setup.py install
git clone https://github.com/blechschmidt/massdns.git ./Tools
cd ./Tools/massdns && make
