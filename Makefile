.PHONY: test

#USER_FUNC=
#SOLUTION=

test:
	PYTHONPATH=. py.test tests --disable-pytest-warnings --verbose --color=yes