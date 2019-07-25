from metaL import *

########################################## Marvin Minsky frame model /extended/

def test_frame_hello():
    hello = Frame('hello')
    assert hello.test() == '<frame:hello>'
    
def test_frame_push():
    hello = Frame('hello')
    assert ( hello // hello ).test() == '<frame:hello>\t<frame:hello> _/'

def test_frame_eval():
    hello = Frame('hello')
    assert hello.eval(hello).test() == '<frame:hello>\t<frame:hello> _/'
