find ./ -maxdepth 1 -name "*.py" -exec sed -i.bak '1i\
#!/usr/bin/python
' {} \;

find . -name "*.bak" -exec rm -rf {} \;