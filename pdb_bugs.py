#!/usr/bin/env python2

filename = __file__

import datetime

class ObtuseWrapper(object):
  
  class WrapperException(Exception):
    """Return when kid rock is mad."""

  """
  This class is a wrapper for some hard-to-discover thing.
  """
  def __init__(self, name=None, state=None, began_career=None):
      """
      Bad Docs.

      Usage: Kid Rock is an ObtuseWrapper.
      """
      super(ObtuseWrapper, self).__init__()
      self.name = name
      self.state = state
      self.began_career = began_career

      # Yes, yes, bad on purpose.
      self.this_year = datetime.datetime.now().year

      self.contemporaries = {}
      self.remaining_relevance = self.career_length()

  def career_length(self):
    return self.this_year - int(self.began_career)

  def shelf_life(self):
    """Any time someone remembers the ObtuseWrapper, their shelf life deteriorates by half."""
    return self.remaining_relevance/2

  def get_contemporaries(self):
    my_range = range(int(self.began_career), self.this_year)

    for year in my_range:
      self.contemporaries[year] = "Uncle Kracker"
      # `Breakpoint to illustrate 'unt' cmd. 
    return self.contemporaries

  def set_contemporary(self, new_artist, year):
    """A better kid rock comes around."""
    try:
      comps = self.contemporaries
      if current_year in comps:
        current_contemporaries[year] = new_artist
    finally:
      print(comps)

kid_rock = ObtuseWrapper(name="Kid Rock", state="MI", began_career="1990")
related_acts = kid_rock.get_contemporaries()
