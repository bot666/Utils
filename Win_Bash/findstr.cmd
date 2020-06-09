@Echo off

set str=%1
set folder=%2

python -c "from bash import *; find_str(" + %str% + "," + %folder% + ")"
