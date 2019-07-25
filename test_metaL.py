from metaL import *

########################################## Marvin Minsky frame model /extended/

class TestFrame:

    def test_hello(self):
        hello = Frame('hello')
        assert hello.test() == '<frame:hello>'
    
    def test_operator_set(self):
        hello = Frame('hello')
        world = Frame('world')
        hello['key'] = world
        assert hello.test() == '<frame:hello>\tkey <frame:world>'

    def test_operator_get(self):
        hello = Frame('hello')
        world = Frame('world')
        hello['key'] = world
        assert hello['key'].test() == '<frame:world>'

    def test_operator_shift(self):
        hello = Frame('hello')
        world = Frame('world')
        hello << world
        assert hello.test() == '<frame:hello>\tworld <frame:world>'

    def test_operator_haskey(self):
        hello = Frame('hello')
        world = Frame('world')
        hello['key'] = world
        hello << world
        assert hello.has('key')
        assert hello.has('world')
        assert not hello.has('nothing')

    def test_operator_push(self):
        hello = Frame('hello')
        world = Frame('world')
        hello // hello // world 
        assert hello.test() == '<frame:hello>\t<frame:hello> _/\t<frame:world>'
    
    def test_stack_dropall(self):
        hello = Frame('hello')
        world = Frame('world')
        hello // hello // world 
        assert hello.dropall().test() == '<frame:hello>'
    
    def test_stack_pop(self):
        hello = Frame('hello')
        world = Frame('world')
        hello // hello // world 
        assert hello.pop().test() == '<frame:world>'
        assert hello.test() == '<frame:hello>\t<frame:hello> _/'
    
    def test_stack_top(self):
        hello = Frame('hello')
        world = Frame('world')
        hello // world 
        assert hello.top().test() == '<frame:world>'
        assert hello.test() == '<frame:hello>\t<frame:world>'
    
    def test_eval(self):
        hello = Frame('hello')
        assert hello.eval(hello).test() == '<frame:hello>\t<frame:hello> _/'
