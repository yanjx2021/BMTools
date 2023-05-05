from xml.dom.pulldom import SAX2DOM
from ...tool import Tool
from gradio_tools.tools import StableDiffusionTool
from gradio_client.client import Job
from gradio_client.utils import QueueError
import time

def build_tool(config) -> Tool:
  tool = Tool(
        "StableDiffusionTool",
        "Image generator",
        name_for_model="stablediffusion_tool",
        description_for_model="An image generator. Use this to generate images based on text input.\nInput should be a description of what the image should look like.\nThe output will be a path to an image file.",
        logo_url="https://your-app-url.com/.well-known/logo.png",
        contact_email="hello@contact.com",
        legal_info_url="hello@legal.com"
    )
  sd = StableDiffusionTool()
  @tool.get("/get_stablediffusion")
  def get_stablediffusion(input : str)-> str:
      job = sd.create_job(input)
      while not job.done():
        status = job.status()
        print(f"\nJob Status: {str(status.code)} eta: {status.eta}")
        time.sleep(30)
      try:
        output = sd.postprocess(job.result())
      except QueueError:
        output = "QUEUE_FULL"
      return output
  return tool