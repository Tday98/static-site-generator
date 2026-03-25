import unittest

from src.textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is random text", TextType.BOLD)
        node2 = TextNode("This is random text", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_CODE_eq(self):
        node = TextNode("for i in range(0,1):", TextType.CODE)
        node2 = TextNode("for i in range(0,1):", TextType.CODE)
        self.assertEqual(node, node2)

    def test_image_eq(self):
        node = TextNode("randomimagelink.jpeg", TextType.IMAGE)
        node2 = TextNode("randomimagelink.jpeg", TextType.IMAGE)
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()