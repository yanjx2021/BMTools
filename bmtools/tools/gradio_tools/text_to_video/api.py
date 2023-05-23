from xml.dom.pulldom import SAX2DOM
from ...tool import Tool
from gradio_tools.tools import TextToVideoTool
from gradio_client.client import Job
from gradio_client.utils import QueueError
import time

def build_tool(config) -> Tool:
  tool = Tool(
        "TextToVideoTool",
        "Video generator based on text.",
        name_for_model="texttovideo_tool",
        description_for_model="A tool for creating videos from text.\nThe input will be a text prompt describing a video scene.\nThe output will be a path to a video file.",
        logo_url="https://your-app-url.com/.well-known/logo.png",
        contact_email="hello@contact.com",
        legal_info_url="hello@legal.com"
    )
  sd = TextToVideoTool()
  @tool.get("/get_texttovideo")
  def get_texttovideo(input : str)-> str:
      return sd.run(input)
  return tool