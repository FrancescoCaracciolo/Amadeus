# Amadeus

This repository contains resources on creating **Amadeus**, the digial copy of **Kurisu Makise** from Steins;Gate. 

Specifically, there are information on how to configure [Nyarch Assistant](https://github.com/NyarchLinux/NyarchAssistant) to behave like Kurisu Makise and tailor it to your needs.

Here is a demo of the expected result, but based on your preferences, you can easily use the existing technologies to customize it to your needs.

[Video Here]

If you want to contribute to this project, please feel free to submit issues and pull requests.

#### Index
- [Directories](#directories)
- [Nyarch Assistant tutorial]()
- [LLM](#llm)
- [Prompting]()
- [Memory and Knowledge]()
- [TTS]()
- [Avatar]()
- [Additional Tools]()

#### Directories
- `Dialogues`: Files contaning Kurisu's lines in the VNs and some context, useful for memory 
- `Extensions`: Newelle/Nyarch Assistant extensions that are made specifically per Kurisu/Amadeus 
- `Prompts`: System prompts in order to make LLMs talk like Kurisu/Amadeus 
- `Voices`: Please **make responsible use of this folder**. Audio files from Kurisu Makise VA. `file.mp3` contains the audio, `file.mp3.txt` contains its transcription. `Voices/README.md` contains more links 
    - `OneShot`: Contains audios for One Shot voice cloning


# Nyarch Assistant tutorial
In this section you can find a quick tutorial on how to configure Nyarch Assistant to achieve similar results to those in the video.

#### 1. Install Nyarch Assistant
Nyarch Assistant can be installed on **any linux distribution using Flatpak**.
Plese note that alternative packaging formats are not supported yet, so just use flatpak.
Once you have your linux distro setup, installation is pretty easy:
1. Install flatpak and flathub, following [this for your distribution](https://flathub.org/setup)
2. Install Nyarch Assistant, following [this section of Nyarch Assistant readme](https://github.com/NyarchLinux/NyarchAssistant?tab=readme-ov-file#installation)

#### 2. Start Nyarch Assistant
Using your application launcher start Nyarch Assistant. In case you don't have one, you can start it using the command `flatpak run moe.nyarchlinux.assistant`.

This is what it should look like on startup:

<img width="1670" height="949" alt="Screenshot From 2025-07-19 15-52-40" src="https://github.com/user-attachments/assets/0cb7faf1-d2e6-448b-bbaa-e6098a994bc8" />

#### 3. Create a new profile
I suggest you to start creating a new profile. Profiles have their own settings, in that way you can always go back to defaults. You can use this feature also to have multiple version of this configuration for multiple use cases. (You have plenty of options so you probably will)

<img width="1430" height="827" alt="Screenshot From 2025-07-19 16-01-50" src="https://github.com/user-attachments/assets/42eb4e3a-d897-478d-bd32-554d7fa6e4d4" />


<img width="1430" height="827" alt="Screenshot From 2025-07-19 16-03-31" src="https://github.com/user-attachments/assets/a19cb311-3afa-48fb-84e2-4ed987df59cb" />

As you can see, she is really happy for her profile name.

#### 4. Choose an LLM
You can choose to use basically any LLM. Any OpenAI compatible model is supported, in addition to Ollama, Gemini, Claude and others. Also, if you want you can set a custom command to run the LLM or make your own extension to add it.

In the demo, `deepseek/deepseek-chat-v3-0324:free` from OpenRouter is used. It is available for free for 50 req/day on OpenRouter, but you can use **whathever model you prefer**, Nyarch Assistant has a lot of providers to choose from, **including local ones**.

To make an informed choice about what model to pick, read the [LLM](#llm) section.

<img width="1440" height="822" alt="Screenshot From 2025-07-19 16-04-26" src="https://github.com/user-attachments/assets/ab293b8d-8202-49af-a35e-e68db5705feb" />



# General Configuration
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




