from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import StreamField

from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from streams import blocks


class EmployeePage(Page):

    profile_image = models.ForeignKey(        
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    work_start = models.DateField(blank=True, null=True)
    bio = RichTextField(features=['h3', 'h4', 'bold', 'italic', 'link'], blank=True, null=True)
    
    position = models.CharField(max_length=500, blank=False, null=False, )
    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('position'),
            FieldPanel('work_start')],
            heading="Данные"),
        ImageChooserPanel('profile_image'),
        FieldPanel('bio')
    ]


class FlexPage(Page):
    """
    Flex page is a common page - intended to be used for legal pages like privacy, about, disclaimer...
    as well as for blog pages
    """

    subpage_types = []
    
    bg_image = models.ForeignKey(
        'wagtailimages.Image', null=True, on_delete=models.SET_NULL, related_name='+'
    )

    content = StreamField(
        [             
            ("richtext", blocks.RichtextBlock()),
            ("video", blocks.VideoBlock()),
            ("figure_w_caption", blocks.FigureWithCaptionBlock()),
        ],
        null=True,
        blank=True,
    )    

    content_panels = Page.content_panels + [
        ImageChooserPanel('bg_image'),
       # FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
        StreamFieldPanel("content"),         
    ]    
    
    class Meta:
        verbose_name = "Страница"
        verbose_name_plural = "Страницы"


class BlogIndexPage(Page):
    '''
    Index page for bezoder.com blog 
    '''
    
    subpage_types = ['flex.FlexPage',]
    max_count = 1

    bg_image = models.ForeignKey(
        'wagtailimages.Image', null=True, on_delete=models.SET_NULL, related_name='+'
    )

    content_panels = Page.content_panels + [
        ImageChooserPanel('bg_image'),       
    ]


