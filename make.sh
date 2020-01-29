if [ $# -eq 0 ] ; then
  echo "Need a commit message!"
  exit 0
fi
commit_message=$1

echo "Iterating version..."
echo ""
version_string=$(python iterate_version.py 2>&1)
sed -i "/\*\*new/c\*\*new in $version_string** : $commit_message" README.md
echo "Executing setup.py..."
echo ""
python setup.py sdist bdist_wheel
echo "Executing git commit..."
echo ""
git add .
git commit -m "$commit_message"
echo "Executing git push..."
echo ""
git push
echo "Executing PyPi update..."
echo ""
./update.sh

