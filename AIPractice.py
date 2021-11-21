#!/usr/bin/env python3

import argparse
import tools.ClassFunctions as ClassFunctions
import importlib
import re
import os

if __name__ == "__main__" :

    parser = argparse.ArgumentParser(prog=os.path.splitext(os.path.basename(__file__))[0])
    subparsers = parser.add_subparsers(help='commands info')

    for file in ClassFunctions.getPluginFiles("Plugins"):
        if file == "__init__.py":
            continue

        """
        1. 使用文件名获取模块名，
        2. 导入模块，
        3. 获取模块同名类，
        4. 获取类方法
        """
        moduleString = file.split(".")[0]
        module = importlib.import_module("Plugins." + moduleString)
        clazz = getattr(module, moduleString)

        clazzDoc = clazz.__doc__
        # 从类注释中获取类说明，也就是帮助
        parser_item = subparsers.add_parser(moduleString, help = clazzDoc.split("@")[0].strip())

        # 从类注释中获取类参数及参数说明，格式@argument: argument doc
        keyValues = {}
        for arg in clazzDoc.split("\n"):
            keyValue = arg.strip().split(":")
            if len(keyValue) == 2 and keyValue[0].strip().startswith("@"):
                keyValues[keyValue[0].strip().replace("@", "")] = keyValue[1].strip()

        # 转换为命令行参数
        for arg in keyValues:
            matchObj = re.match(r'(\S*)\((\S*)\)', arg)
            if matchObj:
                # print("-----------matchObj-----------")
                # print(matchObj.group(1))
                # print(matchObj.group(2))
                # print("------------------------------")
                parser_item.add_argument('-' + matchObj.group(1), default=matchObj.group(2), help=keyValues[arg])
            else:
                parser_item.add_argument('-' + arg, help=keyValues[arg])

        # 获取当前处理方法并设置为该命令的回调函数
        method = getattr(clazz, "run")
        parser_item.set_defaults(func=method)

    #执行函数功能
    args = parser.parse_args()
    if args :
        if len(args.__dict__) > 0:
            print(">>> start call Plugin run or CmdMaps method")
            args.func(args.__dict__)
            print("<<< end call Plugin run or CmdMaps method")
        else:
            parser.parse_args(["-h"])
