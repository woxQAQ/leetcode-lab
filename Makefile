CURRENT_TIME:=$(shell date "+%Y-%m-%d %H:%M:%S")

COMMIT_INFO:=$(shell nu scripts/get-commit-info.nu)

.PHONY: commit
commit:
	@echo "stage and commit"
	@git add .
	@nu scripts/get-commit-info.nu | xargs -0 git commit -m
	@echo "push to origin..."
	@git push
