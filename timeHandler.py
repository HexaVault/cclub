import time
import warnings
import math

def _pluralise(value, amount):
  if (amount == 1): return value
  return value + "s"

class timeHandler:
  def __init__(this):
    this.age = 0
    this.start = 0
    this.init = False
  
  def updateAge(this):
    if not this.init: raise SyntaxError("updateAge called on uninitialised value")
    this.age = time.time() - this.start

  @property
  def timeElapsed(this):
    if not this.init: raise NotImplementedError("timeElapsed was called without being initalised")
    else:
      this.updateAge()
      return this.age
  
  @timeElapsed.setter
  def _setTimeElapsed(this, value):
    if not this.init: raise NotImplementedError("Attempted to call timeElapsed without initalising handler")
    elif not isinstance(value, timeHandler): raise SyntaxError("Attempted to set handler improperly; Try overriding this.age?")
    else:
      this.age = value.age
      this.start = value.start
      this.init = False

  def initalise(this):
    if this.init:
      warnings.warn("Initialised a timer that was already initialised")
    this.init = True
    this.start = time.time()

  def sleepTill(this, inpTime = 0):
    if (this.age < inpTime): time.sleep(inpTime - this.age)
    this.updateAge()
  
  def __str__(this):
    this.updateAge()
    if (this.age < 1): return "<1 second"
    def textHandler(text, time):
      return str(math.floor(time)) + _pluralise(text, math.floor(time))
    if this.age < 60: return textHandler(" second", this.age)
    if this.age < 3600: return ",".join([textHandler(" minute", this.age // 60), textHandler(" second", this.age % 60)])
    return ",".join([textHandler(" hour", this.age // 3600), textHandler(" minute", this.age // 60 % 60), textHandler(" second", this.age % 60)])


  def __eq__(this, comp):
    try:
      this.updateAge(); comp.updateAge(); return this.age == comp.age
    except:
      return False;

  def __int__(this):
    return math.floor(this.age)
  
  def __float__(this):
    return this.age
  
  def __len__(this): raise SyntaxError("Unexpected length call on timeHandler")
  def __iter__(this): raise SyntaxError("Unexpected iterator call on timeHandler")
  def __getitem__(this): raise SyntaxError("Unexpected getitem call on timeHandler")
  def __setitem__(this, alt = 0): raise SyntaxError("Unexpected setitem call on timeHandler")
  def __delitem__(this): raise SyntaxError("Unexpected delitem call on timeHandler")
  def __contains__(this): raise SyntaxError("Unexpected contain call on timeHandler")

  def __iadd__(self, value):
    if isinstance(value, timeHandler):
      self.updateAge(); value.updateAge(); self.age += value.age; self.start -= value.start
    elif type(value) == type(2):
      self.updateAge(); self.age += value; self.start -= value
    else: raise SyntaxError("Invalid iadd operation")
    return self
  
  def __isub__(self, value):
    if isinstance(value, timeHandler):
      self.updateAge(); value.updateAge()
      if (self.age < value.age): raise SyntaxError("Attempted to get negative time")
      self.age -= value.age; self.start += value.start
    elif type(value) == type(2):
      if (self.age < value): raise SyntaxError("Attempted to get negative time")
      self.updateAge(); self.age = self.age - value; self.start = self.start + value
    else: raise SyntaxError("Invalid isub operation")
    return self
  
  def __imul__(self, value): raise SyntaxError("Invalid i- operation called")
  def __itruediv__(self, value): raise SyntaxError("Invalid i- operation called")
  def __imod__(self, value): raise SyntaxError("Invalid i- operation called")
  def __ifloordiv__(self, value): raise SyntaxError("Invalid i- operation called")
  def __ipow__(self, value): raise SyntaxError("Invalid i- operation called")
  def __imatmul__(self, value): raise SyntaxError("Invalid i- operation called")
  