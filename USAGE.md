# 🚀 Get Up & Running with FocusFrameFinder!

Welcome to the express guide to mastering FocusFrameFinder! 🧭✨



## 🧰 Prerequisites

1. Python 3.8 or higher (Because we like to stay updated! 😉)
2.a Python or conda packages: cv2, numpy, os, shutil, tqdm (Don't worry, we'll guide you on how to get these!) 



## 🛠 Setup & Installation

Alright, enough talk, let's get down to business!

1. Fork the repo.
2. Clone the repository: `git clone https://github.com/your-github-handle/focusframefinder.git`
3. Navigate to the cloned directory: `cd focusframefinder`
4. Install necessary packages: `pip install opencv-python numpy tqdm` OR 'conda env create -f environment.yml'
5. If using conda, activate it: conda activate FFF_deblur



## 🕹 How To Use

1. Fire up your terminal and run: `python deblur.py --input-folder /opt/photogrammetry/splitted/areas/South-East --focus-filter 30`
2. Let the program do its thing! It will calculate the focus measure for each image. (Don't worry, we've got a loading bar to keep you company! 🥳)
3. Once done, you'll see some nifty stats about your image focus measures - minimum, maximum, average, and median 📊. This will help you set your blurriness threshold.
4. The images from the input folder are moved to subfolder "blurry" that go below filter value. Good value might be 30? Test it! 🎯.
6. Sit back and relax! 📦.

And voila! You've just given your image sequence a blur-free makeover! 🎉
