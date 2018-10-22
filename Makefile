# Python 
#
PY=python
PYFLAGS=

# Tests
#
TESTIN =
TESTSRC=test/test.py
TESTOUT=

# Esamples
#
RANDIN =
RANDSRC=examples/random.py
RANDOUT=

# Objects
#
default: random
all: test random
#
test: $(TESTSRC) $(TESTIN)
	@echo running $(TESTSRC) with $(PY)
	@$(PY) $(PYFLAGS) $(TESTSRC)
#
random: $(RANDSRC) $(RANDIN)
	@echo running $(RANDSRC) with $(PY)
	@$(PY) $(PYFLAGS) $(RANDSRC)
# force
.PHONY: test

# Clean utils
#
clean-all: clean-libpy clean-test
clean-libpy:
	@cleaning libpy
	@rm -rf libpy/*.pyc libpy/*~
#
clean-test:
	@echo cleaning test
	@rm -rf $(TESTOUT) $(TESTSRC)~
#
clean-rand:
	@echo cleaning random example
	@rm -rf $(RANDOUT) $(RANDSRC)~
