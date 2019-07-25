from metaL import *

########################################## Marvin Minsky frame model /extended/

def test_frame_hello():
    hello = Frame('hello')
    assert hello.test() == '<frame:hello>'
    
def test_frame_operator_set():
    hello = Frame('hello')
    world = Frame('world')
    hello['key'] = world
    assert hello.test() == '<frame:hello>\tkey <frame:world>'

def test_frame_operator_get():
    hello = Frame('hello')
    world = Frame('world')
    hello['key'] = world
    assert hello['key'].test() == '<frame:world>'

def test_frame_operator_shift():
    hello = Frame('hello')
    world = Frame('world')
    hello << world
    assert hello.test() == '<frame:hello>\tworld <frame:world>'

def test_frame_operator_haskey():
    hello = Frame('hello')
    world = Frame('world')
    hello['key'] = world
    hello << world
    assert hello.has('key')
    assert hello.has('world')
    assert not hello.has('nothing')

def test_frame_operator_push():
    hello = Frame('hello')
    world = Frame('world')
    hello // hello // world 
    assert hello.test() == '<frame:hello>\t<frame:hello> _/\t<frame:world>'
    
def test_frame_stack_dropall():
    hello = Frame('hello')
    world = Frame('world')
    hello // hello // world 
    assert hello.dropall().test() == '<frame:hello>'
    
def test_frame_stack_pop():
    hello = Frame('hello')
    world = Frame('world')
    hello // hello // world 
    assert hello.pop().test() == '<frame:world>'
    assert hello.test() == '<frame:hello>\t<frame:hello> _/'
    
def test_frame_stack_top():
    hello = Frame('hello')
    world = Frame('world')
    hello // world 
    assert hello.top().test() == '<frame:world>'
    assert hello.test() == '<frame:hello>\t<frame:world>'
    
def test_frame_eval():
    hello = Frame('hello')
    assert hello.eval(hello).test() == '<frame:hello>\t<frame:hello> _/'
