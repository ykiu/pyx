import unittest
import io
from contextlib import contextmanager
from .. import *

class SimpleTestCase(unittest.TestCase):
  def test_basics(self):
    output = io.StringIO()
    with write_to(output):
      with body():
        with ul():
          for page_name in ['foo', 'bar']:
            with li():
              t(page_name)

    self.assertEqual(
      output.getvalue(),
      '<body>' +
        '<ul>' +
          '<li>' +
            'foo' +
          '</li>' +
          '<li>' +
            'bar' +
          '</li>' +
        '</ul>' +
      '</body>'
    )

  def test_userdefined_element_without_children(self):
    output = io.StringIO()

    @without_children
    def card(title, img_src, description):
      with div():
        with h2():
          t(title)
        with img(src=img_src): None
        with p():
          t(description)


    with write_to(output):
      with card('A cool article', 'coolphoto.jpg', 'This is an awesome article.'):
        None

    self.assertEqual(
      output.getvalue(),
      '<div>' +
        '<h2>' +
          'A cool article' +
        '</h2>' +
        '<img src="coolphoto.jpg">' +
        '</img>' +
        '<p>' +
          'This is an awesome article.' +
        '</p>' +
      '</div>'
    )

  def test_userdefined_element_with_children(self):
    output = io.StringIO()

    @with_children
    def card(date):
      with div(cls='card'):
        yield
        with p(cls='card-date'):
          t(date)

    with write_to(output):
      with card('2018/09/01'):
        with h2():
          t('A cool article')
        with img(src='coolphoto.jpg'): None

    self.assertEqual(
      output.getvalue(),
      '<div class="card">' +
        '<h2>' +
          'A cool article' +
        '</h2>' +
        '<img src="coolphoto.jpg">' +
        '</img>' +
        '<p class="card-date">2018/09/01</p>'
      '</div>'
    )

  def test_null_output(self):
    with self.assertRaises(OutputNotSpecified):
      with div():
        pass
