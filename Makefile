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
example=cannon
EXPLIN =
EXPLSRC=examples/$(example).py
EXPLOUT=examples/$(example).gif

# Objects
#
default: examples
all: test examples
#
test: $(TESTSRC) $(TESTIN)
	@echo running $(TESTSRC) with $(PY)
	@$(PY) $(PYFLAGS) $(TESTSRC)
#
examples: $(EXPLSRC) $(EXPLIN)
	@echo running $(EXPLSRC) with $(PY)
	@$(PY) $(PYFLAGS) $(EXPLSRC)
# force
.PHONY: test examples

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
	@rm -rf $(EXPLOUT) $(EXPLSRC)~ examples/*~
