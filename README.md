# Educational scripts to crawl `sjt.webaula` (some medical courses)

## Disclaimer

I do not endorse or support the use of this software to access illegal material. This project is for educational purpouses only.

## Running

Simply feed a `JSON` file to the `run.sh` script. It will parse the JSON file using `gen_sh.py` which generates a list of `bash` commands to download files and then uses `xargs` to run downloads in parallel.

### Example

 ```
./run.sh ./im0004.json
```

This will download all course material (slides & videos) to `data/im0004`.