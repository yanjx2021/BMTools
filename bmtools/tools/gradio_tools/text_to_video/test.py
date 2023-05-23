from bmtools.agent.tools_controller import load_valid_tools, MTQuestionAnswerer
tools_mappings = {
    'stable_diffusion': "http://127.0.0.1:8079/tools/stable_diffusion/",
    'image_captioning': "http://127.0.0.1:8079/tools/image_captioning/",
    "prompt_generator": "http://127.0.0.1:8079/tools/prompt_generator/",
    "text_to_video": "http://127.0.0.1:8079/tools/text_to_video/",
}

tools = load_valid_tools(tools_mappings)

qa =  MTQuestionAnswerer(openai_api_key='', all_tools=tools)

agent = qa.build_runner()

agent("Create a video for a panda eating bamboo on a rock.")
