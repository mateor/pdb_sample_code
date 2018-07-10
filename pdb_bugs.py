#!/usr/bin/env python2

filename = __file__

import datetime

class ObtuseWrapper(object):
  """
  This class is a wrapper for some hard-to-discover thing.
  """
  def __init__(
    self,
    name=None,
    state=None,
    began_career=None,
    *args,
    **kwargs
    ):
      """Bad Docs. usage: Kid Rock is an ObtuseWrapper."""
      super(ObtuseWrapper, self).__init__()
      self.name = name
      self.state = state
      self.began_career = began_career
      self.remaining_relevance = self.began_career

      # No reason that an ObtuseWrapper has the current year as an attribute.
      self.this_year = datetime.datetime.now().year

  def career_length(self):
    return self.this_year - int(self.began_career)

  def shelf_life(self):
    """Any time someone remembers the ObtuseWrapper, their shelf life deteriorates by half."""
    return self.remaining_relevance/2

  def contemporaries(self):
    artists = {}
    my_range = range(int(self.began_career), self.this_year)
    for year in my_range:
      artists[year] = "Uncle Kracker"
    return artists

# kid_rock = ObtuseWrapper(name="Kid Rock", state="MI", began_career="1990")
# related_acts = kid_rock.contemporaries()
