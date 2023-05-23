from xml.dom.pulldom import SAX2DOM
from ...tool import Tool
from gradio_tools.tools import BarkTextToSpeechTool
from gradio_client.client import Job
from gradio_client.utils import QueueError
import time

SUPPORTED_LANGS = [
    ("English", "en"),
    ("German", "de"),
    ("Spanish", "es"),
    ("French", "fr"),
    ("Hindi", "hi"),
    ("Italian", "it"),
    ("Japanese", "ja"),
    ("Korean", "ko"),
    ("Polish", "pl"),
    ("Portuguese", "pt"),
    ("Russian", "ru"),
    ("Turkish", "tr"),
    ("Chinese", "zh"),
]

SUPPORTED_LANGS = {lang: code for lang, code in SUPPORTED_LANGS}
VOICES = ["Unconditional", "Announcer"]
SUPPORTED_SPEAKERS = VOICES + [p for p in SUPPORTED_LANGS]

NON_SPEECH_TOKENS = [
    "[laughter]",
    "[laughs]",
    "[sighs]",
    "[music]",
    "[gasps]",
    "[clears throat]",
    "'♪' for song lyrics. Put ♪ on either side of the the text",
    "'…' for hesitations",
]

def build_tool(config) -> Tool:
  tool = Tool(
        "BarkTool",
        "Text-to-speech converter",
        name_for_model="bark_tool",
        description_for_model=(
            "A tool for text-to-speech. Use this tool to convert text "
            "into sounds that sound like a human read it. Input will be a two strings separated by a |: "
            "the first will be the text to read. The second will be the desired speaking language. "
            f"It MUST be one of the following choices {','.join(SUPPORTED_SPEAKERS)}. "
            f"Additionally, you can include the following non speech tokens: {NON_SPEECH_TOKENS}"
            "The output will the text transcript of that file."
        ),
        logo_url="https://your-app-url.com/.well-known/logo.png",
        contact_email="hello@contact.com",
        legal_info_url="hello@legal.com"
    )
  sd = BarkTextToSpeechTool()
  @tool.get("/get_bark")
  def bark(input : str)-> str:
      return sd.run(input)
  return tool