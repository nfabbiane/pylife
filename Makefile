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
clean-all: clean-py clean-test clean-examples
clean-py:
	@echo cleaning python files
	@rm -rf libpy/*.pyc libpy/*~
	@rm -rf *.pyc *~
#
clean-test:
	@echo cleaning test
	@rm -rf $(TESTOUT) $(TESTSRC)~
#
clean-examples:
	@echo cleaning examples
	@rm -rf $(RANDOUT) $(RANDSRC)~
