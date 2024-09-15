@ECHO OFF

pushd %~dp0

REM Command file for ALogAnalyze

if "%1" == ""         goto all
if "%1" == "ui"       goto ui
if "%1" == "designer" goto designer
if "%1" == "all"      goto all
if "%1" == "deps"     goto deps

echo.
echo.usage:
echo.	make
echo.	make ui
echo.	make designer
echo.

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

:end
popd
