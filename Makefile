all: build

build:
	cythonize -3 -b -i -j8 -q --lenient -k orion/extras/strings.py
	cythonize -3 -b -i -j8 -q --lenient -k orion/extras/runner.py
