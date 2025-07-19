# Amadeus

This repository contains resources, files and information on how to configure [Nyarch Assistant](https://github.com/NyarchLinux/NyarchAssistant) to behave like Kurisu Makise from Steins;Gate.

Some of these resources **can also be used with other programs**.

If you want to contribute to this project, please feel free to submit issues and pull requests.

#### Directories
- `Dialogues`: Files contaning Kurisu's lines in the VNs and some context, useful for memory 
- `Extensions`: Newelle/Nyarch Assistant extensions that are made specifically per Kurisu/Amadeus 
- `Prompts`: System prompts in order to make LLMs talk like Kurisu/Amadeus 
- `Voices`: Please **make responsible use of this folder**. Audio files from Kurisu Makise VA. `file.mp3` contains the audio, `file.mp3.txt` contains its transcription. `Voices/README.md` contains more links 
    - `OneShot`: Contains audios for One Shot voice cloning
#### Index
- [Nyarch Assistant tutorial]()
- [LLM]()
- [Prompting]()
- [Memory and Knowledge]()
- [TTS]()
- [Avatar]()
- [Additional Tools]()

# Configuration Tutorial

### LLM
#### Models
In order to make an LLM to behave like Kurisu, there are two possible apporaches:
1. Training/Fine Tuning a model specifically to be able to behave like Kurisu
2. Using a general purpose model and specify its behavior via prompting (and some more advanced techniques explained in [Memory and Knowledge]())

While training usually gives the best results, it has a lot of cost/efficiency downsides:
- At the moment of writing (and I doubt in the future), there is no provider offering Amadeus models, meaning that **they must be run locally** or on **providers** that offer running custom models (that are generally much more **expensive**)
- Training is expensive, so generally **models** trained for this **are small**, resulting in **worse performance compared to big models with good prompts**
- LLMs still advance pretty quickly, so trained models might get outdated after a couple of months.


