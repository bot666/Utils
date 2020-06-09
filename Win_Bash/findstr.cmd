@Echo off

cd ..

%str
%folder

python -c 'from bash import *; find_str(' + %str% + ',' + %folder% + ')'
