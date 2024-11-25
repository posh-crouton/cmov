# posh-crouton/cmov 

Inspired by [cloc](https://github.com/AlDanial/cloc), cmov (Count Minutes Of Video) is a command-line utility to find the total duration of videos under a given directory. 

## Usage 
```
$ cmov.py /path/to/your/dir`
```
Optional: 
```
-v|--verbose    Print information as we go
-p|--progress   Show a progress bar 
-s|--seconds    Output the total number of seconds (instead of hh:mm:ss)
```

If you need to use venv, run `src/start.sh` instead of `src/cmov.py`. This will create, set up, activate, and deactivate a virtual environment. 

## Supported file formats
* mp4
* mkv
* avi
* mov
* wmv
* flv
* mpg/mpeg

## License 
MIT no-attribution