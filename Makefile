CURRENT_TIME:=$(shell date "+%Y-%m-%d %H:%M:%S")

COMMIT_INFO:=$(shell nu scripts/get-commit-info.nu | awk '{printf "%s\\n", $$0}' ORS='')

.PHONY: commit
commit:
	echo "stage and commit"
	@git add .
	@git commit -m "${COMMIT_INFO}"
	echo "push to origin..."
	@git push
