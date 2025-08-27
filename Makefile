CURRENT_TIME:=$(shell date "+%Y-%m-%d %H:%M:%S")

COMMIT_INFO:=$(shell nu scripts/get-commit-info.nu)

.PHONY: commit
commit:
	@echo "stage and commit"
	@git add .
	@git commit -m "$(COMMIT_INFO)"
	@echo "push to origin..."
	@git push
