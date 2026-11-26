@echo off
setlocal
cd /d "%~dp0"

call :build neoforge-1.21.1 || exit /b 1
call :build fabric-1.21.8 || exit /b 1
call :build fabric-26.3 || exit /b 1

if not exist dist mkdir dist
copy /y neoforge-1.21.1\build\libs\scale-tooltips-neoforge-1.21.1-1.0.0.jar dist\ >nul
copy /y fabric-1.21.8\build\libs\scale-tooltips-fabric-1.21.8-1.0.0.jar dist\ >nul
copy /y fabric-26.3\build\libs\scale-tooltips-fabric-26.3-1.0.0.jar dist\ >nul

echo Built all three mods in dist\
exit /b 0

:build
pushd %1
call gradlew.bat clean build --no-daemon
set result=%errorlevel%
popd
exit /b %result%
