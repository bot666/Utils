@Echo off

set folder=%1

python -c "from bash import *; ls( %folder% )"
