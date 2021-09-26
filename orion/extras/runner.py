#! /usr/bin/env python3

import shlex, subprocess, tempfile;

def run(cmds:str,stdin:bytes=b'')->any:
    commands:list=shlex.split(cmds);
    buffer:tempfile.SpooledTemporaryFile=tempfile.SpooledTemporaryFile(mode='w+b');
    buffer.write(stdin);
    buffer.seek(0);
    try:
        with subprocess.Popen(commands,stderr=subprocess.PIPE,stdin=buffer,stdout=subprocess.PIPE) as process:
            return process.stdout.read(),process.stderr.read(),process.returncode;
    except Exception as e:
        return 0;
