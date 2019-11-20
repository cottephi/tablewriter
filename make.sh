if [ $# -eq 0 ] ; then
  echo "Need a commit message!"
  exit 0
fi
commit_message=$1

version_string=$(python iterate_version.py 2>&1)
sed -i "/\* new/c\ \* new in $version_string : $commit_message" README.md

python setup.py sdist bdist_wheel
