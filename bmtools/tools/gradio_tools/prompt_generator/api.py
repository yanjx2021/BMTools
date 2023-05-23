from xml.dom.pulldom import SAX2DOM
from ...tool import Tool
from gradio_tools.tools import StableDiffusionPromptGeneratorTool
from gradio_client.client import Job
from gradio_client.utils import QueueError
import time

def build_tool(config) -> Tool:
  tool = Tool(
        "StableDiffusionPromptGeneratorTool",
        "StableDiffusionPromptGenerator",
        name_for_model="promptgenerator_tool",
        description_for_model="An prompt generator. Use this to generate a prompt for stable diffusion and other image and video generators based on text input.\nInput should be a description of what the image should look like.\nThe output will be a generated prompt.",
        logo_url="https://your-app-url.com/.well-known/logo.png",
        contact_email="hello@contact.com",
        legal_info_url="hello@legal.com"
    )
  sd = StableDiffusionPromptGeneratorTool()
  @tool.get("/get_promptgenerator")
  def get_promptgenerator(input : str)-> str:
      return sd.run(input)
  return tool