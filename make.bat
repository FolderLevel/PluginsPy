@ECHO OFF

pushd %~dp0

REM Command file for ALogAnalyze

if "%1" == ""         goto all
if "%1" == "ui"       goto ui
if "%1" == "designer" goto designer
if "%1" == "all"      goto all
if "%1" == "deps"     goto deps
if "%1" == "qt"       goto qt

echo.
echo.usage:
echo.	make
echo.	make all
echo.	make ui
echo.	make qt
echo.	make designer
echo.

goto end

:all
del /s /q dist
pip3 uninstall -y PluginsPy
python3 setup.py sdist bdist_wheel
for %%w in (dist\*.whl) do pip3 install %%w
goto end

:ui
python3 -m PyQt5.uic.pyuic src/PluginsPy/MainUI.ui -o src/PluginsPy/MainUI.py
goto end

:designer
qt5-tools designer
goto end

:deps
pip3 install -r requirements.txt
goto end

:qt
set PYTHONPATH=%cd%\src
python3 tests/test_PluginsPyQT5.py
goto end

:end
popd
