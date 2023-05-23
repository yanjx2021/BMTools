from xml.dom.pulldom import SAX2DOM
from ...tool import Tool
from gradio_tools.tools import DocQueryDocumentAnsweringTool
from gradio_client.client import Job
from gradio_client.utils import QueueError
import time

def build_tool(config) -> Tool:
  tool = Tool(
        "DocQueryDocumentAnsweringTool",
        "Question anwser from the image of the document",
        name_for_model="ducumentanwsering_tool",
        description_for_model="A tool for answering questions about a document from the image of the document.\nInput will be a two strings separated by a |: the first will be the path or URL to an image of a document.The second will be your question about the document.\nThe output will the text answer to your question.",
        logo_url="https://your-app-url.com/.well-known/logo.png",
        contact_email="hello@contact.com",
        legal_info_url="hello@legal.com"
    )
  sd = DocQueryDocumentAnsweringTool()
  @tool.get("/get_qa")
  def get_qa(input : str)-> str:
      return sd.run(input)
  return tool