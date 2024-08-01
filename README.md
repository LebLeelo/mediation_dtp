

# Scientific mediation activity - Object detection on duckiebot

This project will take you through the process of collecting images on a duckiebot and use them to train a neural network to perform object detection using the robot's camera image. 
We will use one of the most popular object detection neural networks, called [YOLO (v5)](https://docs.ultralytics.com/yolov5/). 





# START THE ACTIVITY !🚦️🚦️🚦️🚦️🚦️
Instructions for the activity are available in the following notebook: 📎️ https://colab.research.google.com/drive/1bTHXU9-Cxgmq5Jlo1s1Fg896yTkzNwpm?usp=sharing








# Make sure your system is up-to-date

- 🖥️ Make sure your Duckietown Shell is updated to the latest version. See [installation instructions](https://github.com/duckietown/duckietown-shell)
      Update the shell commands: `dts update`

- 💻 Update your laptop/desktop: `dts desktop update`

- 🛻️ Update your Duckiebot: `dts duckiebot update ROBOTNAME` (where `ROBOTNAME` is the name of your Duckiebot chosen during the initialization procedure.)






# 🛻️ Test on your duckiebot

You can test your agent on the robot using the command,

    dts code workbench --duckiebot YOUR_DUCKIEBOT

This is the modality "everything runs on the robot".

You can also test using

    dts code workbench --duckiebot YOUR_DUCKIEBOT --local 

This is the modality "drivers running on the robot, agent runs on the laptop."


