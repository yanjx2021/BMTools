from ..registry import register

@register("stable_diffusion")
def stable_diffusion():
    from .stable_diffusion import build_tool
    return build_tool