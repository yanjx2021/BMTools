from bmtools.agent.singletool import load_single_tools, STQuestionAnswerer
import pathlib
prompt = "The Action in langchain should follow the format:'Action:API's name'.For example,'Action:get_imagecaption.'"
# Langchain
tool_name, tool_url = 'gradio_tools',  "http://127.0.0.1:8079/tools/gradio_tools/"

tool_name, tool_config = load_single_tools(tool_name, tool_url)

print(tool_name, tool_config)
stqa = STQuestionAnswerer()

agent = stqa.load_tools(tool_name, tool_config)

#test get_promptgenerator+get_stablediffusion+get_imgtomsc
agent("Please create a photo of a dog riding a skateboard but improve my prompt prior to using an image generator.Then create a song from the photo."+prompt)

# test get_texttovideo
agent("Create a video for a panda eating bamboo on a rock.")

# test get_bark+get_promptgenerator+get_stablediffusion
agent("Please create a jingle for a spanish company called 'Chipi Chups' that makes lollipops. "
      "The jingle should be catchy and playful and meant to appeal to all ages.")


IMG_PATH = pathlib.Path(__file__).parent / "florida-drivers-license.jpeg"
#test get_imagecaption
agent(f"Captioning the picture in {IMG_PATH}?"+prompt)
#test get_qa
agent(f"What is the date of birth the driver in {IMG_PATH}?"+prompt)
#test get_imgprompt
agent(f"Creating a prompt for StableDiffusion that matches the input image from {IMG_PATH}?"+prompt)

#test get_audiotrans
AUDIO_PATH = pathlib.Path(__file__).parent / "audio.mp3"
agent(f"Transcribing the audio file track in {AUDIO_PATH} into text"+prompt)