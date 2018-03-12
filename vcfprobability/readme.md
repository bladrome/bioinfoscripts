# vcfprobobility.py
##preprocess
```bash
grep -v '^##' vcffile > vcffile_NoComment
```
##run
```python
python vcfprobobility.py vcffile_NoComment sample_list output.csv
```
