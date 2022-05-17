This is a Python3 wrapper for flvrec.py tool of vnc2flv package that compatible with Python version 2.7.

## Usage

```sh
pip install vnc2flv-rec

vnc2flv localhost port
```

## Create binary

```sh

docker build -t vn2flv-rec-image  .
docker run  --mount type=bind,source="$(pwd)",target=/mnt/  vn2flv-rec-image
```

## License

This project is [MIT Licensed](LICENSE).
