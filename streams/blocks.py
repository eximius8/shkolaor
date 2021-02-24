"""Streamfields live in here."""

from wagtail.core import blocks
from wagtail.embeds.blocks import EmbedBlock
from wagtail.core.templatetags.wagtailcore_tags import richtext
from wagtail.images.blocks import ImageChooserBlock as DefaultImageChooserBlock


class ImageChooserBlock(DefaultImageChooserBlock):
    """
    Image block with serializer
    """

    def get_api_representation(self, value, context=None):
        if value:
            return {
                'id': value.id,
                'title': value.title,
                'large': value.get_rendition('width-1000').attrs_dict,                
            }

class FigureWithCaptionBlock(blocks.StructBlock):
    """Image wrapped in figure tag with figure caption"""

    image = ImageChooserBlock(required=True,  label="Картинка")
    caption = blocks.CharBlock(required=False, help_text = "Подпись к картинке", label="Подпись")

    class Meta:  # noqa
        template = "streams/image_with_caption_block.html"
        icon = "image"
        label = "Картинка с подписью"



class RichtextBlock(blocks.RichTextBlock):
    """Richtext without (limited) all the features."""

    def get_api_representation(self, value, context=None):
        return richtext(value.source)

    def __init__(
        self, required=True, help_text=None, editor="default", features=None, **kwargs
    ):  # noqa
        super().__init__(**kwargs)
        self.features = ['h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'hr', "bold", "italic", "link", 
        'code', 'superscript', 'subscript', 'strikethrough', 'blockquote']

    class Meta:  # noqa
        template = "streams/richtext_block.html"
        icon = "edit"
        label = "Описание"


# https://www.danielms.site/blog/wagtail-embedurl-youtube-tags/
class VideoBlock(blocks.StructBlock):
    """Only used for Video Card modals."""
    video = EmbedBlock() # <-- the part we need

    class Meta:
        template = "streams/video_block.html"
        icon = "media"
        label = "YouTube"

