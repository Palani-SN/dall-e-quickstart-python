# dall-e-quickstart-python

- Sample illustration for usage of Dall-E Image Generation Application using Flask webserver

## How to use

- clone the repo & run **python -m pip install -r requirements.txt --user** from the root folder

- Copy **.env.example** file to create new file named **.env** & Edit the **.env** file inside the **UI/** to add the OpenAI API key

![](https://github.com/Palani-SN/dall-e-quickstart-python/blob/main/images/AddAPIToken.JPG?raw=true)

- change directory to **UI/** in command prompt & Run the webserver using **python frontend.py**

![](https://github.com/Palani-SN/dall-e-quickstart-python/blob/main/images/StepsToRun.JPG?raw=true)

- Go to url **http://127.0.0.1:5000/** 

![](https://github.com/Palani-SN/dall-e-quickstart-python/blob/main/images/HomePage.JPG?raw=true)

- enter the prompt in the text box shown to get an image generated dynamically

![](https://github.com/Palani-SN/dall-e-quickstart-python/blob/main/images/SampleInput.JPG?raw=true)

- click **Generate** to get the results as Image

![](https://github.com/Palani-SN/dall-e-quickstart-python/blob/main/images/Response.JPG?raw=true)

- click **Download** to save the Image

![](https://github.com/Palani-SN/dall-e-quickstart-python/blob/main/images/ResponseImage.png?raw=true)