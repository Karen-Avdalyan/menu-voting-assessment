echo "Linting django project"
echo "[ERRORS]"
echo "----------------------"
find . -type f -name "*.py" | grep -v '^./venv' | xargs pylint --errors-only
echo "----------------------"

