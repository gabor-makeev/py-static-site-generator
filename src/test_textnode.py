import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
  def test_eq(self):
    node = TextNode("This is a text node", TextType.BOLD)
    node2 = TextNode("This is a text node", TextType.BOLD)
    self.assertEqual(node, node2)

  def test_url_none(self):
    node = TextNode("This is a text node", TextType.TEXT)
    self.assertEqual(node.url, None)

  def test_url_not_none(self):
    node = TextNode("This is a text node", TextType.TEXT, "google.com")
    self.assertNotEqual(node.url, None)

  def test_not_eq_text_type(self):
    node = TextNode("This is a text node", TextType.BOLD)
    node2 = TextNode("This is a text node", TextType.ITALIC)
    self.assertNotEqual(node.text_type, node2.text_type)

if __name__ == "__main__":
  unittest.main()