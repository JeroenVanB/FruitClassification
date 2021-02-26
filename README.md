# FruitClassification
Authors: Jeroen van Brandenburg, Daan Krol

Project for the Deep Learning course of the University of Groningen. Several deep architectures, which are pretrained on the ImageNet dataset, are used to classify fruit and vegetables from the Fruit-360 dataset. Resnet50, InceptionV3 and MobileNetv2 are compared in performance. Two optimizers, which implement the Adam and AdaBelief algorithms, are compared in performance when retraining the new classification layers. The impact of data augmentation on the performance of the classifiers is also compared. 

## Running experiments
The ML pipeline can be found in the classify_fruit.ipynb Jupyter notebook.

## Dataset

The original dataset can be found here:[https://www.kaggle.com/moltean/fruits](https://www.kaggle.com/moltean/fruits). The dataset was downloaded on February 12 2021. 

Several subclasses (e.g. Apple Red 1, Apple Red 2) are merged together to great a bigger supperclass (Apples).  
The final class compositions are:  
1.  Apples : Apple Braeburn, Apple Crimson Snow, Apple Golden 1, Apple Golden 2, Apple Golden3, Apple Granny Smith, Apple Pink Lady, Apple Red 1, Apple Red 2, Apple Red 3, Apple RedDelicious, Apple Red Yellow 1 and Apple Red Yellow 2.
2.  Bananas : Banana, Banana Lady Finger and Banana Red.
3.  Cherries :  Cherry 1, Cherry 2, Cherry Rainier, Cherry Wax Black, Cherry Wax Red and CherryWax Yellow
4.  Grapes : Grape Blue, Grape Pink, Grape White, Grape White 2, Grape White 3 and Grape White 4
5.  Onions : Onion Red, Onion Red Peeled and Onion White
6.  Peaches : Peach, Peach 2 and Peach Flat7.  
7.  Pears :  Pear, Pear 2, Pear Abate, Pear Forelle, Pear Kaiser, Pear Monster, Pear Red, Pear Stoneand Pear Williams
8.  Peppers : Pepper Green, Pepper Orange, Pepper Red and Pepper Yellow
9.  Plums : Plum, Plum 2, Plum 3
10. Potatoes : Potato Red, Potato Red Washed, Potato Sweet and Potato White
11. Tomatoes : Tomato 1, Tomato 2, Tomato 3, Tomato 4, Tomato Cherry Red, Tomato Heart, TomatoMaroon, Tomato not Ripened and Tomato Yellow

------- Train -------  
Apples : 6404  
Bananas : 1430  
Cherries : 3444  
Grapes : 3419  
Onions : 1333  
Peaches : 1722  
Pears : 5037  
Peppers : 2478  
Plums : 1767  
Potatoes : 1803  
Tomatoes : 5103  

------- Test -------  
Apples : 2137  
Bananas : 484  
Cherries : 1148  
Grapes : 1146  
Onions : 451  
Peaches : 574  
Pears : 1689  
Peppers : 826  
Plums : 597  
Potatoes : 601  
Tomatoes : 1707  
