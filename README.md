<img width="762" height="698" alt="image" src="https://github.com/user-attachments/assets/39227c1e-b733-4d0a-a67d-57f2cd641489" /># Amadeus

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

#### 5. Choose an Avatar
For the avatar, there are three options supported and showed in the demo:
##### 1. Live2D Avatar

You can download the Live2D avatar [here]() and uncompress it.

After that, go in the settings, go in the Avatar section and scroll down. Expand the Live2D option and click on the folder icon next to the model list:

<img width="762" height="698" alt="Screenshot From 2025-07-21 14-38-51" src="https://github.com/user-attachments/assets/31a5869e-00c1-4fb2-9aea-ee833ef0a5ef" />

Drop the model folder in the opened folder.
<img width="954" height="632" alt="Screenshot From 2025-07-21 14-39-05" src="https://github.com/user-attachments/assets/d3d4bc41-2dc2-4b13-a9ca-a62e71c6c4f4" />

After that refresh the list of models and pick the Amadeus model:

<img width="762" height="698" alt="Screenshot From 2025-07-21 14-39-15" src="https://github.com/user-attachments/assets/d7011356-dd22-4e02-8f21-8032f16c6d91" />

<img width="661" height="595" alt="Screenshot From 2025-07-21 14-40-33" src="https://github.com/user-attachments/assets/8e185e63-628a-4c33-884a-e1ecec790701" />

And here you go. (You can drag the model with the mouse).

<img width="1522" height="922" alt="Screenshot From 2025-07-21 14-41-43" src="https://github.com/user-attachments/assets/66fff0e5-811b-4371-ac15-cb1030c44345" />

##### 2. LivePNG Avatar
LivePNG is the visual novel style. 

Go in the settings, go in the Avatar section and scroll down. Click on the download button

<img width="762" height="698" alt="Screenshot From 2025-07-23 14-48-42" src="https://github.com/user-attachments/assets/80802877-ea6f-43a0-9c79-ad3d54723c41" />

And it will download automatically Kurisu model.
After that, select the model from the settings.

##### 3. Live2D Desktop Pet
This does only work on Gnome wayland and Hyprland at the moment. For installation refer to [this](https://github.com/NyarchLinux/DesktopPuppet).

#### 6. TTS Configuration
For more information about TTS choice read the TTS section.
In the demo, the TTS used is locally run GPTSoVITS with one-shot voice cloning.
For this, you have to install the [Newelle Voice Cloning extension](https://github.com/FrancescoCaracciolo/Newelle-Voice-Cloning).
1. Downlaod the [cloning.py](https://github.com/FrancescoCaracciolo/Newelle-Voice-Cloning/blob/main/cloning.py) file in the repo
2. Open the extensions menu in Nyarch Assistant
<img width="1458" height="840" alt="Screenshot From 2025-07-21 14-42-16" src="https://github.com/user-attachments/assets/aa5c2431-819e-4d4f-89b7-a8e393d75e9f" />

3. Click on Install extension from file
5. Select the cloning.py file
<img width="1012" height="672" alt="image" src="https://github.com/user-attachments/assets/2dda1c0f-81d5-4038-9944-0cd6dc14c7a1" />

After that the extension will be enabled

<img width="622" height="622" alt="image" src="https://github.com/user-attachments/assets/33e0d499-f514-4c68-a4d3-e46123984a32" />


5. Open the settings, go to Avatar and then expand the Text To Speech section and scroll down to SoVITS 2, click on the install button next to it and select it.

<img width="762" height="698" alt="image" src="https://github.com/user-attachments/assets/5e020e7c-31ee-4940-a7be-cf4dc7214597" />
Now, we need to configure it.

#### 7. Prompting 

First of all, disable Smart Prompts. They dinamically add some information about Nyarch Linux in the prompt, but for our puprposes it can make outputs worst.

<img width="762" height="698" alt="image" src="https://github.com/user-attachments/assets/a4118f1c-2bfd-4b47-a493-983eb52367cc" />

I also suggest you to keep off or edit the "helpful assistant" prompt. Kurisu is not very helpful and she doesn't like being called assistant.

Now, let's edit the personality prompt with the prompt you prefer from the **Prompts folder**. In the demo, **"Kurisu_EN.txt"** is used.

I strongly suggest you to have **prompt and expected LLM output in the same language**. You can ask another LLM to translate your prompts into your preferred langauge.

<img width="762" height="698" alt="image" src="https://github.com/user-attachments/assets/56d2dcdf-1baa-451c-878c-d8ff44ec1185" />

You can also choose to translate or edit the other prompts based on your preferences.
I also suggest you to add this prompt in the "Custom Prompt" section:
```
{COND:
[tts_on] Give concise answers, what you say will be spoken out loud
}
```
In this way, when TTS is enabled, the LLM will give short answers.

You can find more about prompting in the [Newelle Wiki](https://github.com/qwersyk/Newelle/wiki/Prompt-variables).

If you want, you can also specify the scenario and give your username putting the {USER} variable in the prompt. (You can set the username in the General settings).

#### 8. Adding Kurisu's Knowledge
In order to give the LLM the memory of Kurisu, we only extract relevant parts from the Steins;Gate Visual Novel script, and put them in the prompt.

First of all, download the dialogue script [here](https://github.com/FrancescoCaracciolo/Amadeus/blob/main/Dialogues/SG_Dialogues_EN.md).

1. Go in the settings, enable knowledge->document folder.
2. Open your documents directory

<img width="762" height="698" alt="image" src="https://github.com/user-attachments/assets/81c0bc1b-d1c4-4901-8821-922a1b5fd06d" />

3. Drop SG_Dialogues_EN.md in that folder
<img width="1150" height="604" alt="image" src="https://github.com/user-attachments/assets/f8209473-ac54-4fed-a68f-932d2c97f679" />

You can also drop there any other file you want as knowledge. If you want, you can also add [SG_Story_EN.md](), in order to give some synthetized knowledge.

I also suggest you to put many limited-length chunks.

Then index your documents (might take some seconds):

<img width="762" height="698" alt="image" src="https://github.com/user-attachments/assets/fac6bd6a-6a0a-4f8b-b1b5-67f3c0d57185" />

When it's done, close the settings. Now some lines from the VN will be added to the prompt, for example:
<img width="1532" height="781" alt="image" src="https://github.com/user-attachments/assets/a2d2b50b-ccdb-4859-bd26-2d4baa1d6b1a" />

#### 9. Speech To Text
For speech to text you can choose anything, it doesn't really change Kurisu's personality.
I suggest to use locally run Whisper.CPP, and also add something like "The user is talking to Kurisu Makise" to the prompt in order to pick the right words. In the demo BASE (EN) Model has been used.

##### Endpoint
First of all, the endpoint. It is where the TTS model is run. By default it runs on [this huggingface space](https://huggingface.co/spaces/XXXXRT/GPT-SoVITS-ProPlus), but it is very slow. I suggest to run it locally if you have a Nvidia GPU.
In order to host the space locally you can install docker on your system (Instructions for Arch, check installtion on your specific distro):
```bash
sudo pacman -S docker nvidia-container-toolkit
sudo systemctl enable --now docker
```
And then run the container:
```bash
sudo docker run -it -p 7860:7860 --platform=linux/amd64 --gpus all \
	registry.hf.space/francescocaracciolo-gpt-sovitsproplus:latest python inference_webui.py
```
If running locally, put in the endpoint: `http://localhost:7860`

##### Reference voice
Reference voice is the voice to clone. 
I suggest you to use the audio in the same language of the output.
You can find some audio files for one shot voice cloning the the [Voices/OneShot directory](https://github.com/FrancescoCaracciolo/Amadeus/tree/main/Voices/OneShot).

After downloading the files, click on the icon folder next to the "Reference Audio" row, drop the files there, click the refresh button and select the audio you want.

Then put the "reference prompt" text (transcription of the reference audio, you can find it in a txt file named like the audio file).
Then select the input and output languages.

The final configuration should look something like this:

<img width="762" height="698" alt="Screenshot From 2025-07-23 15-19-54" src="https://github.com/user-attachments/assets/a9f4728e-5660-432c-a090-52d62f718887" />

If you want the output of the LLM to be in a different language from the LLM, enable the translator:
<img width="762" height="698" alt="Screenshot From 2025-07-23 15-33-10" src="https://github.com/user-attachments/assets/3e0e4a7d-baa1-4bc4-b0bd-d93f80c59554" />



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




