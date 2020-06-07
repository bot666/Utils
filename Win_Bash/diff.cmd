@Echo off

cd ..

%from
%to

python3 -c 'from Bash import *; diff(' + %from% + ',' + %to% + ')'
