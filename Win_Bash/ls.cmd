@Echo off

cd ..

%folder

python -c 'from bash import *; ls(' + %folder% + ')'
