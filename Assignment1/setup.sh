if [ "$(command -v pip)" ]; then
        pip install gzip
elif [ "$(command -v brew)" ]; then
        brew install gzip
fi

python zip_files.py
rm *gz
