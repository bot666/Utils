@Echo off

cd ..

%from
%to

python -c 'from bash import *; diff(' + %from% + ',' + %to% + ')'
