## Another Python implementation of
# THE GAME OF LIFE

(2018) Nicolo Fabbiane

* * *
[![Build Status](https://travis-ci.com/nfabbiane/pylife.svg?branch=master)](https://travis-ci.com/nfabbiane/pylife/builds)
* * *

## Repository structure
+ `life.py`:   **main** library of this Game of Life (GoF) implementation 
+ `libpy/`:    folder of the sources of the sublibraries imported in `life.py`
+ `examples/`: folder of the examples of the usage of the library
+ `tests/`:    folder of the testing tools for the library

## Examples
The examples can be run via the `Makefile`

    make examples example=<name-of-the-example>

### `cannon`: Gosper's gliders cannon
The Gosper's gliders cannon is taken as initial condition.
The output is the file `examples/cannon.gif` that collects in an animated
image the time evolution of the map.

### `rand-init`: simultion from random initial condition
The map is evolved starting from a random initial condition.
The visualisation is based on a simple terminal-based text-output; the same
visualisation technique is used in the tests.

## Tests
The tests can be run via the `Makefile`
    
    make test

and consist in reproducing some known solutions of the GoF, nominally:
- the steady *square* solution
- the period-two *propeller*
- the travelling *glider*

The success of the test is automatically checked by an `assert` command.