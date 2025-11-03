import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
  def test_repr_with_optionals(self):
    expected_result = 'tag = None, value = None, children = None, props = None'
    node = HTMLNode()
    self.assertEqual(expected_result, node.__repr__())

  def test_to_html_exception(self):
    node = HTMLNode()
    with self.assertRaises(NotImplementedError):
      node.to_html()

  def test_props_to_html(self):
    expected_result = ' href="https://www.google.com" target="_blank"'
    node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
    self.assertEqual(node.props_to_html(), expected_result)