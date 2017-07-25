.PHONY: test test2

TEST_PATH = tests/

test:
	@cd $(TEST_PATH) && python test_main.py