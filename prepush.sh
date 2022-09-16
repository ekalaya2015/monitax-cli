echo "export requirements.txt"
poetry export -o requirements.txt --without-hashes
poetry export -o requirements-dev.txt --dev --without-hashes
echo "autoflake"
autoflake --recursive --in-place  \
        --remove-unused-variables \
        --remove-all-unused-imports  \
        --ignore-init-module-imports \
        monitax_cli
echo "black"
black monitax_cli
echo "isort"
isort monitax_cli
echo "flake8"
flake8 monitax_cli --count --statistics
echo "OK"
