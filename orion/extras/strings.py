#! /usr/bin/env python3


def to_string(obj: type):
    return obj if isinstance(obj, str) else obj.decode("utf-8") if isinstance(obj, bytes) else ''
