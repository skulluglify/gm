BASH = /usr/bin/bash
CYTHONIZE = /usr/bin/cythonize

all: build

build: clean
	$(CYTHONIZE) -3 -b -i -j8 -q --lenient -k orion/extras/strings.py
	$(CYTHONIZE) -3 -b -i -j8 -q --lenient -k orion/extras/runner.py

clean:
	$(BASH) CacheCleaner
	$(BASH) RemoveAllPkgs
