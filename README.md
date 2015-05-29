# Earnings
Database of Earnings with around close price

### Installation Guide

##### System Requirements
Make sure your system meets these requirements:
  - Operating system: MacOS 10.7 - 10.10 (it has been tested successfully on these)
  - RAM: 2GB.
  - Disk space: 2GB

##### Step 1: Install Command Line Tools
  - Open terminal, type “xcode-select --install” in terminal (without quotes)
  - A pop-up windows will appear asking you about install tools, choose install tools, wait install to finish
  
##### Step 2: Install Homebrew
  - Copy paste following command to the terminal, and press Enter.
  
  ```
  ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
  ```

##### Step 3: Install Python and its modules
  - Copy paste following commands to the terminal, and press Enter.
  
  ```
  brew install python
  
  pip install numpy
  pip install pandas
  pip install datetime
  pip install quandl
  pip install multiprocessing
  pip install lxml
  pip install apscheduler
  ```

### Running Guide

##### One-time Run:

 - Go to `Earnings` directory at Dropbox and run the python script `download_earnings.py`.

 ```
 cd ~/Dropbox/Earnings
 python download_earnings.py
 ```
 
##### Automatic Run:

  - Go to `Earnings` directory at Dropbox and run the python script `daily_job.py`.

  ```
  cd ~/Dropbox/Earnings
  python daily_job.py
  ```
  
  Never close it, it will run at 17pm every weekday.
