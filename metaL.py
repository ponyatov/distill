## metaL/py : homoiconic metaprogramming system
## (c) Dmitry Ponyatov <dponyatov@gmail.com> CC BY-NC-ND
## wiki: https://github.com/ponyatov/metaL/wiki

import os,sys

############################################ extended Marvin Minsky frame model

class Frame:
    
    def __init__(self,V):
        self.type  = self.__class__.__name__.lower()
        self.val   = V
        self.slot  = {}
        self.nest  = []
        self.immed = False
        
    ## dump
        
    def __repr__(self):
        return self.dump()
    def dump(self, depth=0, prefix='', voc=True):
        tree = self._pad(depth) + self.head(prefix)
        if not depth: Frame._dumped = []
        if self in Frame._dumped: return tree + ' _/'
        else: Frame._dumped.append(self)
        if voc:
            for i in self.slot:
                tree += self.slot[i].dump(depth + 1, prefix= i + ' = ')
        for j in self.nest:
            tree += j.dump(depth + 1)
        return tree
    def head(self, prefix=''):
        return '%s<%s:%s> @%x' % (prefix, self.type, self._val(), id(self))
    def _pad(self, depth):
        return '\n' + ' '*4 * depth
    def _val(self):
        return str(self.val)
    
    ## operator

    ## ` that = this[key] `
    def __getitem__(self,key):
        return self.slot[key]
    ## ` this[key] = that ` 
    def __setitem__(self,key,that):
        self.slot[key] = that ; return self
    ## ` this << that `
    def __lshift__(self,that):
        self[that.val] = that ; return self
    def has(self,key):
        return key in self.slot
    ## ` this // that `
    def __floordiv__(self,that):
        return self.push(that)
        
    ## stack
    
    ## ` ( ... -- ) ` clear
    def dropall(self):
        self.nest = [] ; return self
    ## ` ( -- a ) `
    def push(self,that):
        self.nest.append(that) ; return self
    ## ` ( a b -- a ) `
    def pop(self):
        return self.nest.pop(-1) # b
    ## ` ( a b -- b ) `
    def pip(self):
        return self.nest.pop(-2) # a
    ## ` ( a b -- a b ) `
    def top(self):
        return self.nest[-1] # b
    ## ` ( a b -- a b ) `
    def tip(self):
        return self.nest[-2] # a

    ## ` ( a - a a ) `
    def dup(self):
        return self // self.top()
    ## ` ( a b -- a ) `
    def drop(self):
        self.pop() ; return self
    ## ` ( a b -- b a ) `
    def swap(self):
        return self // self.pip()
    ## ` ( a b -- a b a ) `
    def over(self):
        return self // self.tip()
    ## ` ( a b -- b ) `
    def press(self):
        self.pip() ; return self
    
    ## execute & codegen
    
    def eval(self,ctx):
        return ctx // self
    
    ## special dump form for tests
    
    def test(self,depth=0,prefix=''):
        tree = '\t' * depth + '%s<%s:%s>' % (prefix, self.type, self._val())
        if not depth: Frame._dumped = []
        if self in Frame._dumped: return tree + ' _/'
        else: Frame._dumped.append(self)
        for i in self.slot: tree += self.slot[i].test(depth+1,prefix=i+' ')
        for j in self.nest: tree += j.test(depth+1)
        return tree
    
##################################################################### primitive

class Primitive(Frame): pass

class String(Primitive):
    def _val(self):
        s = ''
        for c in self.val:
            if   c == '\r': s += '\\r'
            elif c == '\n': s += '\\n'
            elif c == '\t': s += '\\t'
            else:           s += c
        return s

class Symbol(Primitive): pass

class Number(Primitive):
    def __init__(self,V):
        Primitive.__init__(self, float(V))

class Integer(Number):
    def __init__(self,V):
        Primitive.__init__(self, int(V))

class Hex(Integer): pass

class Bin(Integer): pass

