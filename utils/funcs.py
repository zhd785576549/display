from importlib import import_module


def get_mod_attr(module_path, attr_name):
    """
    获取模块中的属性
    :param module_path: [str] 模块儿路径
    :param attr_name: [str] 属性名称
    :return:
    """
    mod = import_module(module_path)
    return getattr(mod, attr_name)
