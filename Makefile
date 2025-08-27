CURRENT_TIME:=$(shell date "+%Y-%m-%d %H:%M:%S")

.PHONY: commit
commit:
	git add .
	git commit -m "$$(nu scripts/get-commit-info.nu)"
	git push
