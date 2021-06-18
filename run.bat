pytest -vvv -m "sanity" --html=./reports/reports.html tests/  --browser=chrome
REM pytest -vvv -m "regression" --html=reports/reports.html tests/  --browser=chrome