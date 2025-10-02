# mangaYgoCards
## Special thanks to the [ygoprodeck api](https://ygoprodeck.com/api-guide/)
This program takes in ydk files and makes a pdf of proxies in the style of the ygo manga

### <span style="color:red"> Link and Pendulum monsters will not be transformed but will be added to the proxy pdf </span>


<img src="writeup/34909328.jpg" alt="Ryzeal Detonator" width="300" height="400">
<img src="writeup/62880279.jpg" alt="Dodododo Warrior" width="300" height="400">
<img src="writeup/6595475.jpg" alt="Onomatopaira" width="300" height="400">
<img src="writeup/83326048.jpg" alt="D. Barrier" width="300" height="400">


The output will look like this [this](writeup/proxies.pdf).

# How to use

I recommend getting a [virtual enviroment](https://docs.python.org/3/library/venv.html) set up and running before trying to start the app

After getting a virtual enviroment set up and running, install the requirements.txt 

```
pip install -r requirements.txt
```

After all of this is done you can run this command line and it'll do the rest

```
python main.py [path to .ydk file] [0 if you want to clean up everything or 1 if you want to save the output images]
```


