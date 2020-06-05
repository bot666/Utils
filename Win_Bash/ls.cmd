@Echo off

cd ..

%folder

python3 -c 'from Bash import *; ls(' + %folder% + ')'
