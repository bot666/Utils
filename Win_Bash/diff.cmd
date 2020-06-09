@Echo off

set from=%1
set to=%2

python -c "from bash import *; diff( %from% ,  %to% )"
