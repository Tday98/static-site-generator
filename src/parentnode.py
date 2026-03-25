from .htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("invalid HTML: no tag")
        if self.children is None:
            raise ValueError("invalid HTML: no children")
        ret_string = f"<{self.tag}>"
        for child in self.children:
            # child objects expose a to_html() method
            ret_string += child.to_html()
        ret_string += f"</{self.tag}>"
        return ret_string

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
        