# Model trainer

* **category**    Machine learning  📡
* **author**      Juan Diego Alfonso <jalfons.ocampo@gmail.com>
* **copyright**   [GNU General Public Licence](https://www.gnu.org/licenses/gpl.txt)
* **source**  [GitHub](https://github.com/halcolo/Model_trainer.git)


## Description

This model was created to explain how to train a CNN (Convolutional Neural network) with OpenCV.

## Virtual enviroment

You can create a virtual environment using following commands.

In linux maybe you need the following package `sudo apt-get install python3-venv`

| Description|Linux| Win|
| ------ | ------ |------|
| Install virtenv| `python3 -m pip install --user virtualenv` |`py -m pip install --user virtualenv`|
| Create enviroment | `python3 -m venv modelTrainerEnv` |`py -m venv modelTrainerEnv`|
| Activate enviroment | `source modelTrainerEnv/bin/activate` |`.\modelTrainerEnv\Scripts\activate`|
| Install packages | `pip install --upgrade -r requirements.txt`  |`pip install --upgrade -r requirements.txt` |
| Inactivate  | `deactivate`  | `deactivate`  |

## USE

This app has two parts, the first part is composed by _verifyData.py_ this file show you how OpenCV read the pull if you run `python3 verifyData.py` the app show the image and you can quit the image with "_q_" key.

![:pixeldata:](https://github.com/halcolo/Model_trainer/blob/master/img/pixeldata.png?raw=true ":pixeldata:")

**MATRIX**\
[[224 224 225 ..., 242 242 241]\
 [203 210 219 ..., 243 242 242]\
 [114 106 123 ..., 242 242 242]\
 ...\
 [ 93  96  84 ..., 128 129 129]\
 [ 87  87  84 ..., 122 125 125]\
 [ 74  74  84 ..., 114 106 107]]

 ![:blurdata:](https://github.com/halcolo/Model_trainer/blob/master/img/blurdata.png?raw=true ":blurdata:")

 **MATRIX**\
[[224 224 224 ..., 241 241 241]\
 [224 224 224 ..., 241 241 241]\
 [218 218 218 ..., 241 241 241]\
 ...,\
 [ 78  78  78 ..., 112 112 112]\
 [ 74  74  74 ..., 107 107 107]\
 [ 74  74  74 ..., 107 107 107]]


Next one is the _main.py_ this is the real training, this file read all the pull and add the pull to a list and after that read randomly the list, at the list the lable 0 is the __Matrix__ and the second one is the clasification.


| Aplication| Version|
| ------ | ------ |
| Python| `Python 3.7` |
| OpenCV| `4.1.0` |
| numpy | `1.13.3` |
| tqdm | `4.31.1`  |
| matplotlib| `3.0.3`  |
