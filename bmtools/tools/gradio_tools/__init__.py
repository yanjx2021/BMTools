from ..registry import register

@register("stable_diffusion")
def stable_diffusion():
    from .stable_diffusion import build_tool
    return build_tool
    
@register("bark")
def bark():
    from .bark import build_tool
    return build_tool

@register("prompt_generator")
def prompt_generator():
    from .prompt_generator import build_tool
    return build_tool

@register("text_to_video")
def text_to_video():
    from .text_to_video import build_tool
    return build_tool

@register("image_captioning")
def text_to_video():
    from .image_captioning import build_tool
    return build_tool