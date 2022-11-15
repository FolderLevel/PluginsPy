app := PluginsPy

all:
	pip3 uninstall -y $(app)
	rm -rf dist/*
	python3 setup.py sdist bdist_wheel
	pip3 install dist/$(app)-*-py3-none-any.whl

publish:
	twine upload dist/*

clean:
	pip3 uninstall -y $(app)
