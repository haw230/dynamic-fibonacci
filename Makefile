.PHONY: test

TEST_PATH = tests/

test:
	@cd $(TEST_PATH) && python test_main.py