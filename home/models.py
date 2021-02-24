from django.db import models
from modelcluster.fields import ParentalKey

from wagtail.admin.edit_handlers import (   
    MultiFieldPanel,
    InlinePanel,   
)

from wagtail.core.models import Page, Orderable

from wagtail.images.edit_handlers import ImageChooserPanel

class HomePageCarouselImages(Orderable):
    """Between 1 and 5 images for the home page carousel."""

    page = ParentalKey("home.HomePage", related_name="carousel_images")
    carousel_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    panels = [ImageChooserPanel("carousel_image")]


class HomePage(Page):

    subpage_types = ['flex.BlogIndexPage',]

    max_count = 1
    content_panels = Page.content_panels + [
       
        MultiFieldPanel(
            [InlinePanel("carousel_images", max_num=3, min_num=2, label="Изображение")],
            heading="Carousel Images",
        )       
    ]
