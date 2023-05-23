from xml.dom.pulldom import SAX2DOM
from ...tool import Tool
from gradio_tools.tools import ImageCaptioningTool
from gradio_client.client import Job
from gradio_client.utils import QueueError
import time

def build_tool(config) -> Tool:
  tool = Tool(
        "ImageCaptioningTool",
        "Image captioner",
        name_for_model="imagecaptioning_tool",
        description_for_model="An image captioner. \nInput will be a path to an image file. \nThe output will be a caption of that image.",
        logo_url="https://your-app-url.com/.well-known/logo.png",
        contact_email="hello@contact.com",
        legal_info_url="hello@legal.com"
    )
  sd = ImageCaptioningTool()
  @tool.get("/get_imagecaption")
  def get_imagecaption(input : str)-> str:
      return sd.run(input)
  return tool