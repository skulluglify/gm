#! /usr/bin/env python3

import io, os, shlex, subprocess, signal, tempfile;

class _Template_Popen(object):

    pid: int;
    stdout: io.BytesIO;
    stderr: io.BytesIO;
    returncode: int;

    def __init__(self, stdout:bytes, stderr:bytes, returncode:int):
        self.stdout = io.BytesIO(stdout);
        self.stderr = io.BytesIO(stderr);
        self.returncode = returncode;

    def close(self):
        self.stdout.close();
        self.stderr.close();

class Runner(object):

    listen: bool;
    commands: str;
    buffer: tempfile.SpooledTemporaryFile;
    process: subprocess.Popen;
    stdin: bytes;
    MAXTIMEOUT: int;

    def __init__(self, cmds:str, stdin:bytes=b'', **kwargs):

        ## FEATURES
        # if stdin is io Open, change auto with out tempfile!

        self.listen = False;
        self.MAXTIMEOUT = 5;
        self.stdin = stdin;

        self.__dict__.update(kwargs);
        self.commands = shlex.split(cmds);
        
        if not self.listen:

            self.buffer = tempfile.SpooledTemporaryFile(mode="w+b");
            self.buffer.write(self.stdin);
            self.buffer.seek(0);

            self.process = subprocess.Popen(self.commands, stderr=subprocess.PIPE, stdin=self.buffer, stdout=subprocess.PIPE);

        else:

            self.process = subprocess.Popen(self.commands, stderr=subprocess.PIPE, stdin=subprocess.PIPE, stdout=subprocess.PIPE);

    def start(self) -> subprocess.Popen:

        if self.listen:
            T:_Template_Popen=_Template_Popen(*self.process.communicate(input=self.stdin,timeout=self.MAXTIMEOUT), self.process.returncode);
            T.pid = self.process.pid;
            return T;
            
        T:_Template_Popen=_Template_Popen(b'', b'', self.process.returncode);
        T.close();

        T.stdout = self.process.stdout;
        T.stderr = self.process.stderr;
        T.pid = self.process.pid;

        return T;

    def __enter__(self) -> subprocess.Popen:
        return self.start();

    def __exit__(self, exception_type:any, exception_value:any, traceback:any):
        self.close();

    def close(self):
    
        if hasattr(self, "buffer"): self.buffer.close();

        self.process.terminate();
        self.process.kill();
        
    def terminate(self):
        os.kill(self.process.pid, signal.SIGKILL | signal.SIGQUIT | signal.SIGTERM);

    def kill(self):
        self.terminate();
