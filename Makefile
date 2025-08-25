
CURRENT_TIME:=$(shell date +%Y-%m-%d_%H:%M:%S)

.PHONY: commit
commit:
	git add .
	git commit -m "solution update $(CURRENT_TIME)"
	git push
