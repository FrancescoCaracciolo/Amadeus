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

### TTS
For TTS, you can choose to use a generic TTS, or a TTS obtained using voice cloning of Kurisu's voice actor.

In case you choose to use a generic TTS, it is suggested to use "Kokoro TTS" (locally run, open source and very fast even on CPU and well supported on Nyarch Assistant with amazing sound quality), or Edge TTS (closed, online only but fast and good quality).

Other options are using [ElevenLabs](https://elevenlabs.io/) (one of the highest quality TTS, closed and payment only), and [Deepgram](https://deepgram.com/) (nice quality, closed, but with 200$ free credit on registration, use it with this [extension](https://github.com/FrancescoCaracciolo/NewelleExtensions/blob/main/extensions/deepgram.py)).

#### Voice Cloning 
**Please, don't use voice cloning for bad things**

For voice cloning there are three possible approaches:
1. Fine-tune a voice cloning model 
2. Use a one-shot voice cloning model (clone from just 10s of audio)
3. Use a generic TTS + RVC voice conversion to make it sound like Kurisu 

##### One Shot voice cloning 
There are multiple models that support one shot voice cloning in Newelle in this [repository](https://github.com/FrancescoCaracciolo/Newelle-Voice-Cloning).
In the demonstration, GPT-SoVITS is used.


##### Fine Tuning 
There is still no tutorial or model made for this. You can find a dataset for training in Japanese in the Voices folder.

##### TTS + Voice Conversion
I have not written an extension to do this yet, but I plan it in the future.

### Avatar 
For avatar, Nyarch Assitant supports natively:
- Live2D (usually used by VTubers)
- LivePNG (Format made specifically for Newelle, VN Style)
Both support expressions.

### Additional tools 
Nyarch Assistant has support for many tools, form code execution to web search. Also, Newelle extensions are fully supported.

In addition to that here are some extensions to introduce some tools specifically for Amadeus:

#### Divergence Meter
The divergence meter allows the AI to check the divergence value from [https://divergence.nyarchlinux.moe](https://divergence.nyarchlinux.moe), that tries to estimate the divergence of the current worldline using world news. 




