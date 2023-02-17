# hw09
## reading temp values
there's a python script temp_read.py that'll read all 3 temp sensors and dump their data to console
## logging to sheets
for some reason it's not working on my end but i tried quite a bit. 
sheets is here https://docs.google.com/spreadsheets/d/1gHHZa-khr3Kst3za644zx9EgiQSm9lSFfkpT7AWzc38/edit#gid=0
error is below
| Traceback (most recent call last):
| File "/home/debian/exercises/iot/google/sheets/./demo.py", line 73, in <module>
|   main()
| File "/home/debian/exercises/iot/google/sheets/./demo.py", line 54, in main
|   creds = flow.run_console()
| AttributeError: 'InstalledAppFlow' object has no attribute 'run_console'

## logging temps to sheets
simple combination of demo.py and temp_read.py. will be done soon tm. 