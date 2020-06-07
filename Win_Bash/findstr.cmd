@Echo off

cd ..

%str
%folder

python3 -c 'from Bash import *; find_str(' + %str% + ',' + %folder% + ')'
