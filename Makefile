app := pluginspy
DOCSLINES     = $(strip $(shell find src/PluginsPy -iname "*.py" | xargs cat | wc -l | tail -n 1 | awk -F " " '{print $$1}') | sed ':a;s/\([0-9]\{1,\}\)\([0-9]\{3\}\)/\1,\2/g;ta')

all:
	pip3 uninstall -y $(app)

	rm -rf dist/*
	rm -rf src/PluginsPy/template/output
	find * -iname __pycache__ | xargs rm -rf
	
	python3 setup.py sdist bdist_wheel
	pip3 install dist/$(app)-*-py3-none-any.whl

publish:
	twine upload dist/*

clean:
	pip3 uninstall -y $(app)

ui:
	python3 -m PyQt5.uic.pyuic src/PluginsPy/MainUI.ui -o src/PluginsPy/MainUI.py

qt:
	export PYTHONPATH=${PYTHONPATH}:`pwd`/src && python3 tests/test_PluginsPyQT5.py

count:
	@echo docs lines: $(DOCSLINES)
