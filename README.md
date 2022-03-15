# Auto Arranger Based on Deep Learning Methods
## Introduction
  While writing music guitar players often need to try how their guitar part would sound in full arrangement. But rarely they play other musical instruments, drums or bass guitar for example. This project implements the idea of automatic accompaniment. There is no need to worry about backing track anymore, as user can create it by simply choosing music style. The gets guitar notes as an input and then automatically generates parts for drums and bass guitar. 
  
  In contrast to existing auto arrangement products, in this project deep learning is used to create accompaniment without using samples. It allows to train program to compose music for almost any instrument in any style. The key advantage of using machine learning is that the program learns from real music, which makes result sound natural. 
  
  We have tried more than 20 different data preparation approaches and four types of neural networks, ranging from basic dense model to deep recurrent ones. For now, the best result has been achieved using LSTM (Long Short-Term Memory – type of recurrent neural networks). We have already trained model on 24 classic rock groups and 8 rock and roll groups. Parts written by the neural network are over 70% identical to the parts composed by original performers. 
  
  The program can be trained in every needed music style, as there are open libraries of guitar tablatures available. 

## How to use
For using program you should run qt_form.py and all the packages used should be installed first.

There is an exaples folder, where you can find:
* GuitarPro and .mp3 files with bass guiatar and drums parts created by our model.
* Screenshots of program.
